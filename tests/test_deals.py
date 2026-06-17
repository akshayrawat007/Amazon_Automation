import allure
import pytest
from pages.deals_page import DealsPage
from pages.search_page import SearchPage
from config.config import BASE_URL, load_test_data, DEALS_URL
from utilities.screenshot_manager import ScreenshotManager


class TestDeals:

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_deals_page_available_deals(self, driver):
        deals_page = DealsPage(driver)
        deals_page.open_deals_page()
        count = deals_page.get_deals_count()
        with allure.step("Validating deals"):
            assert count > 0, "Deals page should display at least one deal"

    @pytest.mark.regression
    def test_validate_products_minimum_results(self, driver):
        data = load_test_data("search_data.json")
        search_page = SearchPage(driver)
        for product in data["search_products"]:
            driver.get(BASE_URL)
            search_page.search_product(product["keyword"])
            results_count = search_page.get_search_results_count()
            if results_count < product["min_options"]:
                search_page.log_error(f"{product['keyword']} returned {results_count} results, "
                    f"expected at least {product['min_options']}"
                )
            assert results_count >= product["min_options"], (
                f"{product['keyword']} should have at least {product['min_options']} results"
            )

    @pytest.mark.sanity
    def test_filter_deals_by_category(self, driver):
        data = load_test_data("search_data.json")
        deals_page = DealsPage(driver)
        for category in data["deal_categories"]:
            driver.get(DEALS_URL)
            deals_page.filter_by_category(category)
            deals_page.take_screenshot("Category found")
            deals_page.wait.wait_for_dom_to_load()
