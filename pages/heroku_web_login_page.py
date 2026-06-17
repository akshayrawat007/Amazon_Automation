from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import HEROKU_LOGIN_PAGE_URL


class HerokuLoginPage(BasePage):

    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")
    LOGOUT_BUTTON = (By.PARTIAL_LINK_TEXT,'Logout')


    def navigate_to_login_page(self):
        self.log_step("Opening Heroku login page")
        self.driver.get(HEROKU_LOGIN_PAGE_URL)

    def login(self, username, password):
        self.log_step(f"Logging in with username: {username}")
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)

    def is_login_successful(self):
        logout_button = self.find_element(self.LOGOUT_BUTTON)
        assert logout_button.is_enabled() , "Logout Button not enabled"
        return self.is_element_present(self.SUCCESS_MESSAGE)

    def is_login_failed(self):
        return self.is_element_present(self.ERROR_MESSAGE)
