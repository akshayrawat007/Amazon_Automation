
import pytest
from pages.search_page import SearchPage
import logging

logger = logging.getLogger(__name__)


@pytest.mark.regression
def test_add_product_to_cart(driver):
    driver.get("https://www.amazon.com/")
    search_page = SearchPage(driver)
    search_page.search_product("Laptop")
    search_page.wait_for_visibility(search_page.SEARCH_RESULTS)
    search_page.click_first_product()
    driver.switch_to.window(driver.window_handles[-1])
    search_page.add_to_cart()
    logger.info("Product added to cart")
    search_page.take_screenshot("product_added_to_cart")
    success_message = search_page.wait_for_visibility(search_page.SUCCESS_ADD_TO_CART)
    assert "Added to cart" in success_message.text
