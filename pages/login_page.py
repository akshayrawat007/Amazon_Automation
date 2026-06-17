import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from dotenv import load_dotenv
load_dotenv()
import allure

class LoginPage(BasePage):
    HELLO_SIGN_IN = (By.CLASS_NAME,'nav-line-1-container')
    CUSTOMER_SIGN_IN = (By.LINK_TEXT,'Sign in')
    AMAZON_LOGO = (By.CLASS_NAME,'a-link-nav-icon')
    COUNTRY_DROPDOWN = (By.XPATH,"//span[contains(@class,'a-dropdown-prompt')]")
    INDIA_OPTION = (By.XPATH,"//a[@role='option' and contains(@data-value,'IN')]")
    CONTINUE_BUTTON = (By.CLASS_NAME,'a-button-input')
    INPUT_MAIL = (By.ID,'ap_email_login')
    INPUT_PASS = (By.ID,'ap_password')
    INPUT_SUBMIT = (By.ID,'signInSubmit')
    ACCOUNT= (By.LINK_TEXT,'Your Account')


    @allure.step("Login operation in amazon")
    def account_login(self):
        self.log_step(f"Login process started")
        self.wait.explicit_wait(self.HELLO_SIGN_IN,condition="clickable")
        self.actions.hover_element(self.HELLO_SIGN_IN)
        self.click_element(self.CUSTOMER_SIGN_IN)
        self.wait.explicit_wait(self.AMAZON_LOGO,condition="visible")
        self.send_keys(self.INPUT_MAIL,os.getenv("EMAIL_ID"))
        #When dealing with log in using mobile number
        # self.click_element(self.COUNTRY_DROPDOWN)
        # self.click_element(self.INDIA_OPTION)
        self.click_element(self.CONTINUE_BUTTON)
        self.send_keys(self.INPUT_PASS,os.getenv("PASSWORD"))
        self.click_element(self.INPUT_SUBMIT)
        print("Login successful")


