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
