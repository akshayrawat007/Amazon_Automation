import logging

from utilities.action_utils import ActionUtils
from utilities.screenshot_manager import ScreenshotManager
from utilities.wait_utils import WaitUtils

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)
        self.actions = ActionUtils(driver)

    def find_element(self, locator):
        try:
            return self.wait.explicit_wait(locator,condition="visible")

        except Exception as e:
            logger.error(f"Element not found: {locator}. Error: {str(e)}")
            self.take_screenshot(f"element_not_found")
            raise

    def find_elements(self, locator):
        try:
            return self.wait.explicit_wait(locator,condition="elements_visible")
        except Exception as e:
            logger.error(f"Elements not found: {locator}. Error: {str(e)}")
            return []

    def wait_for_visibility(self, locator):
        try:
            return self.wait.explicit_wait(locator,condition="visible")
        except Exception as e:
            logger.error(f"Element not visible: {locator}")
            self.take_screenshot(f"element_not_visible")
            raise

    def wait_for_clickable(self, locator):
        try:
            return self.wait.explicit_wait(locator,condition="clickable")
        except Exception as e:
            logger.error(f"Element not clickable: {locator}")
            self.take_screenshot(f"element_not_clickable")
            raise

    def wait_for_invisibility(self, locator):
        try:
            return self.wait.explicit_wait(locator,condition="invisibility")
        except Exception as e:
            logger.warning(f"Element still visible: {locator}")
            return False

    def click_element(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            element.click()
        except Exception as e:
            logger.error(f"Failed to click element: {locator}. Error: {str(e)}")
            self.take_screenshot(f"click_failed")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            logger.error(f"Failed to send keys to element: {locator}. Error: {str(e)}")
            self.take_screenshot(f"send_keys_failed")
            raise

    def get_text(self, locator):
        try:
            element = self.find_element(locator)
            return element.text
        except Exception as e:
            logger.error(f"Failed to get text from element: {locator}")
            return None

    def scroll_to_element(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logger.info(f"Scrolled to element: {locator}")
        except Exception as e:
            logger.error(f"Failed to scroll to element: {locator}")
            raise

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logger.info("Scrolled to bottom")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        logger.info("Scrolled to top")

    def get_elements_count(self, locator):
        try:
            elements = self.find_elements(locator)
            return len(elements)
        except:
            return 0

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def execute_script(self, script, *args):
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            logger.error(f"Failed to execute script: {str(e)}")
            raise

    def js_click(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            logger.error(f"Failed to JS click element: {locator}")
            raise

    def switch_to_frame(self, locator):
        try:
            frame = self.find_element(locator)
            self.driver.switch_to.frame(frame)
        except Exception as e:
            logger.error(f"Failed to switch to frame: {locator}")
            raise

    def switch_out_of_frame(self):
        self.driver.switch_to.default_content()
        logger.info("Switched out of frame")

    def get_element_attribute(self, locator, attribute):
        try:
            element = self.find_element(locator)
            return element.get_attribute(attribute)
        except Exception as e:
            logger.error(f"Failed to get attribute: {attribute}")
            return None

    def accept_alert(self):
        try:
            self.driver.switch_to.alert.accept()
        except Exception as e:
            logger.error(f"Failed to accept alert: {str(e)}")
            raise

    def dismiss_alert(self):
        try:
            self.driver.switch_to.alert.dismiss()
        except Exception as e:
            logger.error(f"Failed to dismiss alert: {str(e)}")
            raise

    def get_alert_text(self):
        try:
            return self.driver.switch_to.alert.text
        except Exception as e:
            logger.error(f"Failed to get alert text: {str(e)}")
            return None

    def take_screenshot(self, step_name):
        return ScreenshotManager.capture_screenshot(self.driver,step_name)

    def log_step(self, message):
        logger.info(f"STEP: {message}")

    def log_error(self, message):
        logger.error(f"ERROR: {message}")

