# Data Cleaning & Deduplication in Python

## Project Overview
This project demonstrates how to clean a dataset by identifying and removing duplicate records using Python. Ensuring data accuracy and consistency is critical for any data analysis workflow.

## Problem Statement
The dataset contained duplicate entries, which could lead to incorrect analysis. The goal was to:
1. Identify duplicate records.
<img width="957" height="364" alt="image" src="https://github.com/user-attachments/assets/538422f6-49e7-4e13-8de0-96e1b6a39f91" />

2. Remove duplicates while keeping one unique record.
USE df_cleaned = df.drop_duplicates()

3. Save the cleaned dataset.
<img width="957" height="335" alt="image" src="https://github.com/user-attachments/assets/851e4383-8885-4827-a28b-b53c24b84754" />


## Solution Approach

### Step 1: Load the Dataset
```python
import pandas as pd

# Load dataset
df = pd.read_excel('dataset.xlsx')
print("Original Data:")
print(df)

Step 2: Identify Duplicates
# Find duplicate rows
duplicates = df[df.duplicated()]
print("Duplicate rows:")
print(duplicates)


Step 3: Remove Duplicates
# Drop duplicate rows and keep the first occurrence
df_cleaned = df.drop_duplicates()
print("Data after removing duplicates:")
print(df_cleaned)


Step 4: Save Cleaned Data
# Save cleaned dataset to a new file
df_cleaned.to_excel('cleaned_dataset.xlsx', index=False)
print("Cleaned dataset saved as 'cleaned_dataset.xlsx'.")

```

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
DME (8).md…]()
```

# HT Folder Organizer (Google Apps Script)

**Project type:** Automation / Google Workspace (Clinic operations)

## Summary
This script reads patient rows from a Google Sheet (including a Drive folder link and an HT Date) and organizes patient folders into a **Year → Month → Day** hierarchy in Google Drive. It copies each patient folder into the correct date folder. The script supports **resume logic** to handle Apps Script execution time limits.

<img width="765" height="281" alt="image" src="https://github.com/user-attachments/assets/f88222bb-9518-40b1-a3a7-c65262f910d1" />


> ⚠️ **Privacy:** All patient data must be anonymized before adding to this repository. Do not push real patient-identifying data.

---

## What it solves
Clinic staff uploaded patient documents to Drive without a consistent folder structure. Finding records by date was time-consuming. This automation saves hours by building a consistent date-based structure automatically.

**Before:** scattered patient folders  
**After:** `DriveRoot / 2023 / 07 / 29 / <patient_folder>`

---

## Files in this folder
- `Code.gs` — Google Apps Script (main automation code)
- `sample_data.csv` — anonymized example input (columns match the Sheet)
- `README.md` — this file

---

## How to run (quick)
**Option A: Paste in Apps Script editor (manual)**
1. Open Google Sheets with your data.
2. Tools → Script editor.
3. Replace the default code with contents of `Code.gs`.
4. Edit `rootDestinationFolderId` at the top to your destination folder id.
5. Save, run `organizeByHTDate` (first run will ask for permissions).
6. Optionally run `createTimeDrivenTrigger()` to run automatically every 5 minutes.

<img width="959" height="436" alt="image" src="https://github.com/user-attachments/assets/68f9476d-a85c-474d-90be-a68c79629e30" />


**Option B: Use clasp (source-managed approach)**  
Use `clasp` to push code from this repo to an Apps Script project. (Search `clasp` docs if unfamiliar.)

---

## Required Sheet format (example headers)
You can use `sample_data.csv` as template. Important columns:
- `Name`
- `Type`
- `Created Date`
- `Last Modified Date`
- `Link` (Google Drive folder link)
- `Root Folder`
- `HT Date` (dd/MM/yyyy or a Date object)
- `Video Link`
- `File/Folder Count`
- `Structure`
<img width="947" height="205" alt="image" src="https://github.com/user-attachments/assets/321f91cb-80ca-40d1-aa51-d737ce1dc75b" />

---

## Safety & troubleshooting
- The script copies folders so it needs Drive authorization (`DriveApp` scope). Approve when prompted.
- If Apps Script times out (6 minutes), the resume feature will continue from the last saved row on next run.
- Ensure `rootDestinationFolderId` belongs to the account running the script or is shared properly.

---

## Demo assets (recommended)
- Add a before/after screenshot of Drive structure: `before.png`, `after.png`.
- Record a small GIF showing a single folder being copied into the Year/Month/Day path and display in the README:
  ```markdown
  ![demo](./demo.gif)



