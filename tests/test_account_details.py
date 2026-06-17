import os

import pytest

from pages.account_page import AccountPage
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_validation(driver):
    account_page = AccountPage(driver)
    driver.get(os.getenv("BASE_URL"))
    login_page = LoginPage(driver)
    login_page.account_login()
    login_page.actions.hover_element(login_page.HELLO_SIGN_IN)
    login_page.click_element(login_page.ACCOUNT)
    account_page.account_details_prime_membership()
