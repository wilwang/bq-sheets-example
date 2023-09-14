# Reading an BigQuery external table linked to Google Drive Sheets
1. service account needs to have at least Viewer access to sheet
2. service account requires BigQuery User / BigQuery Data Viewer roles
3. requires using Drive scope to access Sheets otherwise you get a 403 error on Drive credentials
4. enable Drive API and BigQuery API on the cloud project

