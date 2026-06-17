import os

import pytest
from pages.search_page import SearchPage
import logging
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)


@pytest.mark.sanity
@pytest.mark.smoke
def test_search_product(driver):
    driver.get(os.getenv("BASE_URL"))
    search_page = SearchPage(driver)
    search_page.search_product("laptop")
    assert search_page.is_results_displayed(), "Search results should be displayed"
    results_count = search_page.get_search_results_count()
    assert results_count > 0, "Search results count should be greater than 0"
    logger.info(f"Test passed: Found {results_count} products")
    search_page.take_screenshot("search_results_displayed")
