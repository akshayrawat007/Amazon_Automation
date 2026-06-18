import gspread
from google.oauth2.service_account import Credentials
from config.config import GOOGLE_SERVICE_ACCOUNT, GOOGLE_SHEET_ID
import logging

logger = logging.getLogger(__name__)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
]


class GoogleSheetUtils:

    def __init__(self):
        creds = Credentials.from_service_account_file(GOOGLE_SERVICE_ACCOUNT, scopes=SCOPES)
        client = gspread.authorize(creds)
        self.spreadsheet = client.open_by_key(GOOGLE_SHEET_ID)
        logger.info(f"Connected to Google Sheet: {self.spreadsheet.title}")

    def get_all_rows_as_dict(self, sheet_name):
        sheet = self.spreadsheet.worksheet(sheet_name)
        rows = sheet.get_all_records()
        logger.info(f"Loaded {len(rows)} rows from sheet: {sheet_name}")
        return rows

    def get_cell_value(self, sheet_name, row, col):
        sheet = self.spreadsheet.worksheet(sheet_name)
        value = sheet.cell(row, col).value
        logger.info(f"Cell ({row},{col}) from '{sheet_name}': {value}")
        return value

    def get_column_values(self, sheet_name, col):
        sheet = self.spreadsheet.worksheet(sheet_name)
        values = sheet.col_values(col)
        logger.info(f"Column {col} from '{sheet_name}': {len(values)} values")
        return values

    def get_row_count(self, sheet_name):
        sheet = self.spreadsheet.worksheet(sheet_name)
        return sheet.row_count