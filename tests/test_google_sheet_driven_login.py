import pytest
from pages.heroku_web_login_page import HerokuLoginPage
from utilities.google_sheets_manager import GoogleSheetUtils


def load_login_data_from_sheet():
    sheet = GoogleSheetUtils()
    return sheet.get_all_rows_as_dict("LoginData")


class TestLoginGoogleSheetDriven:

    @pytest.mark.sanity
    @pytest.mark.parametrize("credentials", load_login_data_from_sheet())
    def test_login_with_google_sheet_data(self, driver, credentials):
        username = credentials["username"]
        password = credentials["password"]
        expected = credentials["expected_result"]
        page = HerokuLoginPage(driver)
        page.navigate_to_login_page()
        page.login(username, password)

        if expected == "pass":
            page.take_screenshot("login_success")

            if not page.is_login_successful():
                page.log_error(f"Expected login success for user: {username}")
            assert page.is_login_successful(), f"Login should pass for user: {username}"

        elif expected == "fail":
            page.take_screenshot("login_failure")
            if not page.is_login_failed():
                page.log_error(f"Expected login failure for user: {username}")
            assert page.is_login_failed(), f"Login should fail for user: {username}"