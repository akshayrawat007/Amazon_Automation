from utilities.google_sheets_manager import GoogleSheetUtils

sheet = GoogleSheetUtils()
rows = sheet.get_all_rows_as_dict("LoginData")
print(f"Connected successfully. Rows found: {len(rows)}")
for row in rows:
    print(row)