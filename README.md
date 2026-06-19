# Automation Framework

A lightweight Selenium-based UI automation framework using pytest and the Page Object Model (POM). It includes Allure reporting, Google Sheets data-driven tests, and reusable utilities for stable, maintainable tests.

## Checklist

- [x] Understand project purpose and layout
- [x] Install dependencies
- [x] Configure environment and credentials
- [x] Run tests locally or via batch scripts
- [x] Generate and open Allure reports

## Project Highlights

- Test runner: pytest
- Design pattern: Page Object Model (pages/)
- Reporting: Allure (reports/allure-results → reports/allure-report)
- Test data: local JSON (testdata/) and Google Sheets integration (utilities/google_sheets_manager.py)
- Utilities: screenshots, wait helpers, action helpers (utilities/)

## Requirements

- Python 3.8+ recommended
- Google service account JSON for Google Sheets tests (service_account.json)

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

- `pytest.ini` — pytest configuration (markers, Allure directory)
- `conftest.py` — fixtures and WebDriver setup
- `config/config.py` — project constants and paths
- `.env` — environment variables used by the framework (BASE_URL, credentials, GOOGLE_SHEET_ID, etc.)
- `service_account.json` — Google API credentials for Google Sheets (place in project root)

Set any required environment variables or update `.env` before running Google Sheets driven tests.

## How to run

Run all tests:

```powershell
pytest tests/
```

Run tests by marker:

```powershell
pytest tests/ -m sanity
pytest tests/ -m regression
pytest tests/ -m smoke
```

Run a single test file:

```powershell
pytest tests/test_login.py
```

Use the provided batch scripts on Windows (interactive):

```powershell
.\run.bat        # interactive menu: All / Sanity / Regression / Smoke / Google Sheets
.\run2.bat tests/test_dummy.py   # direct runner; accepts an optional test path
```

Generate and open Allure report (Allure must be installed on your PATH):

```powershell
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

## Google Sheets driven tests

1. Create a Google service account and download `service_account.json` to the project root.
2. Share the target Google Sheet with the service account email.
3. Provide the sheet ID in environment or `.env` as `GOOGLE_SHEET_ID`.

Run the Google Sheets driven test file:

```powershell
pytest tests/test_dummy.py
```

## Where to look in the code

- `pages/` — Page object classes for each page under test
- `tests/` — pytest test cases grouped by feature
- `utilities/` — helpers (actions, waits, screenshots, Google Sheets manager)
- `config/config.py` — central config
- `conftest.py` — fixtures, WebDriver lifecycle, screenshot on failure
- `requirements.txt` — pinned dependencies

## Reporting & Artifacts

- Screenshots on failure: saved to `screenshots/` and attached to Allure reports
- Allure results: `reports/allure-results`
- Final Allure report: `reports/allure-report`

## Tips

- Use markers to run focused test subsets during development.
- Keep `service_account.json` out of source control — it contains sensitive credentials.
- If WebDriver issues occur, check `webdriver-manager` usage and ensure compatible browser versions.

## Contributing

1. Follow the existing Page Object pattern when adding new pages under `pages/`.
2. Add tests under `tests/` and mark them with one of the markers defined in `pytest.ini`.
3. Keep utilities generic and reusable.

---
