from time import sleep

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from dotenv import load_dotenv


load_dotenv()

class AccountPage(BasePage):
    TOAD_MESSAGE = (By.XPATH,"//h1[normalize-space()='Your Account']")
    PRIME = (By.XPATH,"//div[@data-card-identifier='PrimeConsumer']")
    MEMBERSHIP_DETAILS = (By.XPATH,'//h1[@data-prime-customer-name-fallback-key="heading"]')
    START_TRIAL = (By.ID,'plp-hero-cta')
    PAYMENT_METHOD = (By.XPATH,"//h1[normalize-space()='Select a payment method']")

    @allure.step("Validate prime membership")
    def account_details_prime_membership(self):
        self.log_step("Checking prime membership")
        message = self.find_element(self.TOAD_MESSAGE).text
        assert "Account" in message
        self.find_element(self.PRIME)
        self.click_element(self.PRIME)
        text = self.get_text(self.MEMBERSHIP_DETAILS)
        assert "free 30-day trial" in text
        self.click_element(self.START_TRIAL)
        self.is_element_present(self.PAYMENT_METHOD)








