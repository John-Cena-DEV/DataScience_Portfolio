#!/usr/bin/env python3
"""
sync_folders.py - Synchronize two folders (images) and optionally remove duplicates.

Usage examples:
  python sync_folders.py --folder-a "/path/to/A" --folder-b "/path/to/B" --dry-run
  python sync_folders.py --parent-dir "/path/to/parent" --recursive
  python sync_folders.py --folder-a A --folder-b B --delete-duplicate --force-delete

Features:
 - Copy missing files both directions so folders end up with the same set of files.
 - Safe conflict handling (if same filename differs in content, incoming file is renamed).
 - Dry-run mode to preview actions without changing files.
 - Recursive mode to include subdirectories.
 - Auto-scan mode to detect likely duplicate folder pairs in a parent directory.
"""
import os
import shutil
import argparse
import hashlib
import logging
import time
import re

def setup_logger(log_path=None, verbose=True):
    logger = logging.getLogger("sync_folders")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    if logger.hasHandlers():
        logger.handlers.clear()
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO if verbose else logging.WARNING)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    if log_path:
        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

def file_md5(path, block_size=65536):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(block_size), b""):
            h.update(chunk)
    return h.hexdigest()

def get_all_files(root, recursive=False):
    root = os.path.abspath(root)
    files = {}
    if recursive:
        for dirpath, dirnames, filenames in os.walk(root):
            rel_dir = os.path.relpath(dirpath, root)
            for fname in filenames:
                rel = os.path.normpath(os.path.join(rel_dir, fname)) if rel_dir != "." else fname
                files[rel.replace(os.sep, "/")] = os.path.join(dirpath, fname)
    else:
        for fname in os.listdir(root):
            p = os.path.join(root, fname)
            if os.path.isfile(p):
                files[fname] = p
    return files

def normalize_folder_name(name):
    name = name.lower().strip()
    name = re.sub(r'(\s*\(copy\)|\s*\(1\)|_copy|-copy|_duplicate|-duplicate|\s*\(dup\))$', '', name)
    name = re.sub(r'[^a-z0-9]', '', name)
    return name

def find_folder_pairs(parent_dir):
    parent_dir = os.path.abspath(parent_dir)
    entries = [d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))]
    groups = {}
    for d in entries:
        key = normalize_folder_name(d)
        groups.setdefault(key, []).append(os.path.join(parent_dir, d))
    pairs = []
    for key, paths in groups.items():
        if len(paths) > 1:
            for i in range(len(paths)):
                for j in range(i+1, len(paths)):
                    pairs.append((paths[i], paths[j]))
    return pairs

def copy_or_move(src, dest, move=False, dry_run=False):
    dest_dir = os.path.dirname(dest)
    os.makedirs(dest_dir, exist_ok=True)
    if dry_run:
        return True, f"DRY RUN: {'move' if move else 'copy'} {src} -> {dest}"
    if move:
        shutil.move(src, dest)
        return True, f"moved {src} -> {dest}"
    else:
        shutil.copy2(src, dest)
        return True, f"copied {src} -> {dest}"

def sync_pair(folder_a, folder_b, recursive=False, dry_run=False, move=False, match_by_hash=False, logger=None):
    if logger is None:
        logger = setup_logger()
    logger.info(f"Scanning folders:\n  A: {folder_a}\n  B: {folder_b}\n  recursive={recursive}")
    files_a = get_all_files(folder_a, recursive=recursive)
    files_b = get_all_files(folder_b, recursive=recursive)
    set_a = set(files_a.keys())
    set_b = set(files_b.keys())

    missing_in_a = sorted(list(set_b - set_a))
    missing_in_b = sorted(list(set_a - set_b))

    logger.info(f"Files in A: {len(files_a)}; Files in B: {len(files_b)}")
    logger.info(f"Missing in A: {len(missing_in_a)}; Missing in B: {len(missing_in_b)}")

    actions = []

    if match_by_hash:
        logger.info("Computing file hashes for content-based matching (may be slow)...")
        # Hash maps (hash -> list of (rel, path))
        hash_a = {}
        for rel, path in files_a.items():
            try:
                h = file_md5(path)
            except Exception as e:
                logger.warning(f"Failed to hash {path}: {e}")
                continue
            hash_a.setdefault(h, []).append((rel, path))
        hash_b = {}
        for rel, path in files_b.items():
            try:
                h = file_md5(path)
            except Exception as e:
                logger.warning(f"Failed to hash {path}: {e}")
                continue
            hash_b.setdefault(h, []).append((rel, path))
        # Note: this script does not automatically rename files to match names across folders;
        # it uses content hashes primarily to detect identical files (to skip copying or to detect conflicts).

    # Copy missing files from B -> A
    for rel in missing_in_a:
        src = files_b.get(rel)
        dest = os.path.join(folder_a, rel)
        if os.path.exists(dest):
            try:
                if file_md5(src) == file_md5(dest):
                    logger.info(f"File {rel} exists in destination and is identical; skipping.")
                    actions.append(f"skip identical {rel}")
                    continue
                else:
                    base, ext = os.path.splitext(os.path.basename(rel))
                    new_name = f"{base}_from_B_{int(time.time())}{ext}"
                    dest = os.path.join(folder_a, os.path.dirname(rel), new_name) if os.path.dirname(rel) else os.path.join(folder_a, new_name)
                    logger.warning(f"Conflict for {rel}; will save incoming file as {os.path.relpath(dest, folder_a)}")
            except Exception as e:
                logger.warning(f"Error comparing files for {rel}: {e}")
        ok, msg = copy_or_move(src, dest, move=move, dry_run=dry_run)
        logger.info(msg)
        actions.append(msg)

    # Copy missing files from A -> B
    for rel in missing_in_b:
        src = files_a.get(rel)
        dest = os.path.join(folder_b, rel)
        if os.path.exists(dest):
            try:
                if file_md5(src) == file_md5(dest):
                    logger.info(f"File {rel} exists in destination and is identical; skipping.")
                    actions.append(f"skip identical {rel}")
                    continue
                else:
                    base, ext = os.path.splitext(os.path.basename(rel))
                    new_name = f"{base}_from_A_{int(time.time())}{ext}"
                    dest = os.path.join(folder_b, os.path.dirname(rel), new_name) if os.path.dirname(rel) else os.path.join(folder_b, new_name)
                    logger.warning(f"Conflict for {rel}; will save incoming file as {os.path.relpath(dest, folder_b)}")
            except Exception as e:
                logger.warning(f"Error comparing files for {rel}: {e}")
        ok, msg = copy_or_move(src, dest, move=move, dry_run=dry_run)
        logger.info(msg)
        actions.append(msg)

    return actions

def main():
    parser = argparse.ArgumentParser(description="Sync two folders and optionally remove duplicate folder.")
    parser.add_argument("--folder-a", help="Path to folder A")
    parser.add_argument("--folder-b", help="Path to folder B")
    parser.add_argument("--parent-dir", help="Parent directory to auto-find duplicate folder pairs (scan mode)")
    parser.add_argument("--recursive", action="store_true", help="Include files in subdirectories")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--move", action="store_true", help="Move files instead of copying")
    parser.add_argument("--match-by-hash", action="store_true", help="Use file content hashes to help resolve conflicts")
    parser.add_argument("--delete-duplicate", action="store_true", help="Delete the second folder after syncing (USE WITH CAUTION)")
    parser.add_argument("--force-delete", action="store_true", help="Force delete without extra confirmation (use with --delete-duplicate)")
    parser.add_argument("--log", help="Path to write a detailed log file", default="sync_folders.log")
    parser.add_argument("--verbose", action="store_true", help="Verbose console output")
    args = parser.parse_args()

    logger = setup_logger(args.log, verbose=args.verbose)

    if args.parent_dir:
        pairs = find_folder_pairs(args.parent_dir)
        if not pairs:
            logger.info("No candidate duplicate folder pairs found in parent directory.")
            return
        logger.info(f"Found {len(pairs)} folder pair(s) to process.")
        for a, b in pairs:
            logger.info(f"Processing pair:\n  A: {a}\n  B: {b}")
            actions = sync_pair(a, b, recursive=args.recursive, dry_run=args.dry_run, move=args.move, match_by_hash=args.match_by_hash, logger=logger)
            logger.info(f"Actions taken: {len(actions)} for pair {os.path.basename(a)} <-> {os.path.basename(b)}")
            if args.delete_duplicate:
                if args.force_delete or (not args.dry_run and input(f"Delete duplicate folder '{b}'? [y/N]: ").lower() == 'y'):
                    if not args.dry_run:
                        shutil.rmtree(b)
                        logger.info(f"Deleted folder {b}")
                    else:
                        logger.info(f"DRY RUN: Would delete {b}")
    else:
        if not args.folder_a or not args.folder_b:
            logger.error("Please provide --folder-a and --folder-b, or --parent-dir for scan mode.")
            parser.print_help()
            return
        actions = sync_pair(args.folder_a, args.folder_b, recursive=args.recursive, dry_run=args.dry_run, move=args.move, match_by_hash=args.match_by_hash, logger=logger)
        logger.info(f"Actions taken: {len(actions)}")
        if args.delete_duplicate:
            if args.force_delete or (not args.dry_run and input(f"Delete duplicate folder '{args.folder_b}'? [y/N]: ").lower() == 'y'):
                if not args.dry_run:
                    shutil.rmtree(args.folder_b)
                    logger.info(f"Deleted folder {args.folder_b}")
                else:
                    logger.info(f"DRY RUN: Would delete {args.folder_b}")

if __name__ == "__main__":
    main()
