import os

import pytest

from pages.login_page import LoginPage
from config.config import BASE_URL



@pytest.mark.smoke
def test_login_validation(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.account_login()
    assert driver.title == "Amazon.com. Spend less. Smile more."
