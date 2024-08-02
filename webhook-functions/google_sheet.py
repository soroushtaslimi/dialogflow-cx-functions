# pip install oauth2client
# pip install google-api-python-client

# sheet_id: is the ID of the sheet obtainable from the sheet URL
# credentials_file: is the json object downloaded from the service account

# Note: You need to share your google sheet with the email address of the service account for this to work.

from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleSheetManager:
    def __init__(self, sheet_id, credentials_file):
        self.sheet_id = sheet_id
        credentials = service_account.Credentials.from_service_account_file(credentials_file)  
        self.service = build('sheets', 'v4', credentials=credentials)

    def read_sheet(self, sheet_name):
        range_ = f'{sheet_name}!A1:Z'
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.sheet_id,
            range=range_,
        ).execute()
        values = result.get('values', [])
        return values # containing both the header and all the rows

    def write_sheet(self, sheet_name, values):
        range_ = f'{sheet_name}!A1:Z'
        result = self.service.spreadsheets().values().update(
            spreadsheetId=self.sheet_id,
            range=range_,
            valueInputOption='USER_ENTERED',
            body={'values': values}
        ).execute()
        return result.get('updatedCells')
