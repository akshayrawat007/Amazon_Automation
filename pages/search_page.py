from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import allure
logger = logging.getLogger(__name__)


class SearchPage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    SEARCH_RESULTS = (By.XPATH, "//div[@data-component-type='s-search-result']")
    PRODUCT_TITLE = (By.XPATH,".//a//h2")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    SUCCESS_ADD_TO_CART = (By.XPATH,"//h1[normalize-space()='Added to cart']")

    @allure.step("Search for a product i.e {product_name}")
    def search_product(self, product_name):
        self.log_step(f"Searching for product: {product_name}")
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click_element(self.SEARCH_BUTTON)
        self.log_step("Search completed")

    @allure.step("Get search results count")
    def get_search_results_count(self):
        try:
            results = self.find_elements(self.SEARCH_RESULTS)
            return len(results)
        except:
            return 0

    def is_results_displayed(self):
        return self.is_element_present(self.SEARCH_RESULTS)

    def click_first_product(self):
        self.log_step("Clicking first product")
        try:
            results = self.find_elements(self.SEARCH_RESULTS)
            if results:
                first_product = results[0].find_element(*self.PRODUCT_TITLE)
                first_product.click()
            else:
                logger.error("No search results found")
        except Exception as e:
            logger.error(f"Failed to click first product: {str(e)}")
            raise

    @allure.step("Add product to cart123")
    def add_to_cart(self):
        self.log_step("Adding product to cart")
        try:
            self.click_element(self.ADD_TO_CART_BUTTON)
            self.take_screenshot("product_added_to_cart")
        except Exception as e:
            logger.error(f"Failed to add product to cart: {str(e)}")
            raise
