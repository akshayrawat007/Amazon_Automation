import pytest
import allure

from pages.deals_page import DealsPage


@pytest.mark.sanity

@pytest.mark.smoke
def test_available_deals(driver):
    deals_page = DealsPage(driver)
    driver.get("https://www.amazon.com/deals")
    count = deals_page.get_deals_count()
    with allure.step("Validating deals"):
        assert count > 0, "Deals page should display at least one deal"