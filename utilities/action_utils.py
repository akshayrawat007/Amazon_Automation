from selenium.webdriver import ActionChains
import logging

logger = logging.getLogger(__name__)

class ActionUtils:

    def __init__(self,driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def move_the_slider(self, locator, x_offset):
        slider = self.driver.find_element(*locator)
        ActionChains(self.driver).drag_and_drop_by_offset(slider,
            x_offset, 0).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        (self.actions.click_and_hold(source)
            .move_to_element(target)
            .release()
            .perform()
        )

    def hover_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            self.actions.move_to_element(element).perform()
            logger.info(f"Hovered over element: {locator}")
        except Exception as e:
            logger.error(f"Failed to hover element: {locator}")
            raise