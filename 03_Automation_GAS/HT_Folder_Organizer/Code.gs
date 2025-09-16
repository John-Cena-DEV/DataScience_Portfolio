
---

# 3) Add the Apps Script code (copy into `Code.gs`)
This is your script improved with:
- resume via `PropertiesService`
- time-safety check (stop before timeout)
- trigger creation / clearing helpers
- robust logging and anonymized-safe comments

```javascript
/**
 * HT Folder Organizer
 * Reads rows from the active sheet and copies a source Drive folder into
 * Year/Month/Day -> <source folder name>
 *
 * IMPORTANT:
 * - Set rootDestinationFolderId to your target Drive folder id.
 * - The sheet should have HT Date in column index 8 (I) according to the screenshot.
 */

/* ========= CONFIG ========= */
var ROOT_DESTINATION_FOLDER_ID = "PASTE_YOUR_ROOT_FOLDER_ID_HERE"; // <-- SET THIS
var SHEET_NAME = ""; // leave empty to use active sheet; or set exact sheet name
var HT_DATE_COL = 8;   // zero-indexed (A=0). Column I in your screenshot => index 8
var SOURCE_LINK_COL = 4; // Column E in your screenshot => index 4
/* ========================== */

function organizeByHTDate() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = SHEET_NAME ? ss.getSheetByName(SHEET_NAME) : ss.getActiveSheet();
  var dataRange = sheet.getDataRange();
  var data = dataRange.getValues();

  var rootDestinationFolder = DriveApp.getFolderById(ROOT_DESTINATION_FOLDER_ID);
  var props = PropertiesService.getScriptProperties();
  var startRow = parseInt(props.getProperty("lastProcessedRow")) || 1; // resume; 0-based index in our loop uses i
  var startTime = new Date().getTime();
  var maxRunMillis = 5 * 60 * 1000 - 20 * 1000; // stop ~20s before 6-minute limit

  for (var i = startRow; i < data.length; i++) {
    try {
      // time check — exit early so we can resume next run
      if (new Date().getTime() - startTime > maxRunMillis) {
        Logger.log("Approaching time limit. Saving progress at row: " + i);
        props.setProperty("lastProcessedRow", i);
        return;
      }

      var row = data[i];
      var htDate = row[HT_DATE_COL];
      var sourceLink = row[SOURCE_LINK_COL];

      if (!htDate || !sourceLink) {
        // skip if no date or link
        continue;
      }

      var dateObj = parseDateFromSheet(htDate);
      if (!dateObj) {
        Logger.log("Invalid HT Date at row " + (i+1) + ": " + htDate);
        continue;
      }

      var year = dateObj.getFullYear().toString();
      var month = ("0" + (dateObj.getMonth() + 1)).slice(-2);
      var day = ("0" + dateObj.getDate()).slice(-2);

      var yearFolder = getOrCreateFolder(rootDestinationFolder, year);
      var monthFolder = getOrCreateFolder(yearFolder, month);
      var dayFolder = getOrCreateFolder(monthFolder, day);

      // extract folderId from link
      var folderIdMatch = sourceLink.toString().match(/[-\w]{25,}/);
      if (!folderIdMatch) {
        Logger.log("Invalid Drive link at row " + (i+1) + ": " + sourceLink);
        continue;
      }
      var sourceFolder = DriveApp.getFolderById(folderIdMatch[0]);
      var targetFolder = getOrCreateFolder(dayFolder, sourceFolder.getName());

      // copy contents
      copyFolderContents(sourceFolder, targetFolder);

      Logger.log("Copied row " + (i+1) + " -> " + year + "/" + month + "/" + day + "/" + sourceFolder.getName());

      // Save progress (next index)
      props.setProperty("lastProcessedRow", (i + 1).toString());

    } catch (err) {
      Logger.log("Error at row " + (i+1) + ": " + err);
      // continue to next row (optionally set lastProcessedRow here to retry failed row later)
      props.setProperty("lastProcessedRow", (i + 1).toString());
    }
  }

  // done - clear progress marker
  props.deleteProperty("lastProcessedRow");
  Logger.log("All rows processed.");
}

/** Parse date from sheet cell that may be a Date object or 'dd/MM/yyyy' string */
function parseDateFromSheet(cell) {
  if (!cell) return null;
  if (Object.prototype.toString.call(cell) === "[object Date]") return cell;
  var s = cell.toString().trim();
  var parts = s.split("/");
  if (parts.length === 3) {
    var d = parseInt(parts[0], 10);
    var m = parseInt(parts[1], 10) - 1;
    var y = parseInt(parts[2], 10);
    return new Date(y, m, d);
  }
  // try ISO parse fallback
  var iso = new Date(s);
  if (!isNaN(iso.getTime())) return iso;
  return null;
}

function getOrCreateFolder(parent, name) {
  var folders = parent.getFoldersByName(name);
  if (folders.hasNext()) return folders.next();
  return parent.createFolder(name);
}

function copyFolderContents(source, destination) {
  // copy files
  var files = source.getFiles();
  while (files.hasNext()) {
    var f = files.next();
    f.makeCopy(f.getName(), destination);
  }
  // recurse into subfolders
  var folders = source.getFolders();
  while (folders.hasNext()) {
    var sub = folders.next();
    var newSub = getOrCreateFolder(destination, sub.getName());
    copyFolderContents(sub, newSub);
  }
}

/* ===== Helpers: Trigger management & debug ===== */

function createTimeDrivenTrigger() {
  // create a time-based trigger to run every 5 minutes
  ScriptApp.newTrigger('organizeByHTDate')
    .timeBased()
    .everyMinutes(5)
    .create();
  Logger.log("Time-driven trigger created (every 5 minutes).");
}

function deleteAllTriggersForFunction() {
  var all = ScriptApp.getProjectTriggers();
  for (var i = 0; i < all.length; i++) {
    var t = all[i];
    if (t.getHandlerFunction() === 'organizeByHTDate') {
      ScriptApp.deleteTrigger(t);
    }
  }
  Logger.log("Deleted triggers for organizeByHTDate.");
}
