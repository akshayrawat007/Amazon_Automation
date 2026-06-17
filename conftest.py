import allure

import pytest
from selenium import webdriver
from dotenv import load_dotenv

from utilities.screenshot_manager import ScreenshotManager

load_dotenv()


class DriverSetup:

    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-notifications')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)
        return driver

@pytest.fixture(scope='function')
def driver():
    print("\n Setting up chrome driver ")
    driver = DriverSetup.get_driver()
    yield driver
    print("\n Tearing down of chrome driver")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]
        screenshot_path = ScreenshotManager.capture_screenshot_on_failure(driver, item.nodeid)
        if screenshot_path:
            allure.attach.file(
                screenshot_path,
                name=f"{item.name}_failure_ss",
                attachment_type=allure.attachment_type.PNG
            )