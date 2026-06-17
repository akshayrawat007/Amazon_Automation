import os
import json
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TESTDATA_PATH = "testdata"
DEALS_URL = os.getenv("DEALS_URL")

GOOGLE_CREDENTIALS_DATA= os.getenv("GOOGLE_CREDENTIALS_DATA")
HEROKU_LOGIN_PAGE_URL = os.getenv("HEROKU_LOGIN_PAGE_URL")
GOOGLE_SHEET_ID= os.getenv("GOOGLE_SHEET_ID")

def load_test_data(file_name):
    file_path = os.path.join(TESTDATA_PATH, file_name)
    with open(file_path) as f:
        return json.load(f)