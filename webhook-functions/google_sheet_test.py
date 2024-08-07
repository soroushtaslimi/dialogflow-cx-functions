from google_sheet import GoogleSheetManager
import os

sheet_id = "1GJKFrXgyPWngS4Uz44z_xuu3nXOJdywOY8tBsF8F_Jg"
credentials_file = os.path.join("credentials", "google_doc_cred", "credentials.json")
sheet_name = "Sheet1"

google_sheet_manager = GoogleSheetManager(sheet_id, credentials_file)

doc_val = google_sheet_manager.read_sheet(sheet_name)
print(doc_val)

