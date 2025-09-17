# Folder Deduplication & File Synchronization

## Project Overview
Automated reconciliation of duplicate folders containing images (or other files). When two folders contained similar but mismatched sets of photos, I built a Python tool to:
- Detect missing files between folders,
- Copy or move missing files so both folders contain the same set of files,
- Handle filename conflicts safely,
- Optionally delete the redundant folder after sync.

<img width="954" height="180" alt="image" src="https://github.com/user-attachments/assets/e8513860-0c61-4739-9d6b-71a71231db00" />

This saved a lot of manual time and ensured a consistent dataset.

## How it works (short)
1. Scan both folders and list files (optionally recursive for subfolders).
2. Compute the difference: which files are present in B but missing in A and vice versa.
3. Copy missing files from the other folder. If a filename conflict occurs and files differ by content, the incoming file is renamed (keeps both).
4. Optionally delete the duplicate folder after verifying the sync (requires confirmation).

<img width="860" height="194" alt="image" src="https://github.com/user-attachments/assets/914c9c55-d4b7-4dee-83b0-00b02c32e416" />


## Features
- Dry-run mode to preview changes (`--dry-run`).
- Recursive syncing of nested directories (`--recursive`).
- Move instead of copy (`--move`) if you want to consolidate files.
- Auto-discover duplicate folders inside a parent directory (`--parent-dir`).
- Log file generation (`sync_folders.log` by default).
- Safe conflict handling (renames incoming files to avoid overwriting).
- Optional `--delete-duplicate` (use `--force-delete` to skip confirmation).

## Quick Setup
1. Put `sync_folders.py` in a folder (e.g., `folder-deduplication-sync/`).
2. (Optional) Create a `logs/` folder for logs, or leave default log location.
3. Make sure Python 3.x is installed.

## Usage Examples

**Dry-run between two folders (safe preview):**
```bash
python sync_folders.py --folder-a "/path/to/Folder_A" --folder-b "/path/to/Folder_B" --dry-run --recursive
Actually sync (copy missing files both directions):

python sync_folders.py --folder-a "/path/to/Folder_A" --folder-b "/path/to/Folder_B" --recursive
Move files (instead of copying) and then delete duplicate folder B after confirmation:

python sync_folders.py --folder-a "/path/to/Folder_A" --folder-b "/path/to/Folder_B" --move --delete-duplicate
Auto-scan a parent directory for likely duplicate folder pairs (based on normalized names):


python sync_folders.py --parent-dir "/path/to/parent" --recursive --dry-run
Force delete duplicate folder (USE WITH CAUTION):

python sync_folders.py --folder-a A --folder-b B --delete-duplicate --force-delete
