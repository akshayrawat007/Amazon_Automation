from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import DEALS_URL


class DealsPage(BasePage):

    DEAL_CARDS = (By.XPATH, "//div[@data-csa-c-item-type='deal']")
    CATEGORY_FILTER = (By.XPATH,"//div[contains(@class,'Carousel-module__carousel')]//button")

    def open_deals_page(self):
        self.log_step("Opening deals page of Amazon Website")
        self.driver.get(DEALS_URL)

    def get_deals_count(self):
        self.log_step("Getting deals count")
        count = self.get_elements_count(self.DEAL_CARDS)
        if count == 0:
            self.log_error("No deals found on page")
        return count

    def filter_by_category(self, category_name):
        self.log_step(f"Filtering deals by category: {category_name}")
        filters = self.find_elements(self.CATEGORY_FILTER)
        for option in filters:
            category_text = option.text.strip()
            if category_text.lower() == category_name.lower():
                self.log_step(f"Found category: {category_name}")
                option.click()
                return True
        self.log_error(f"Category filter not found: {category_name}")
        return False


