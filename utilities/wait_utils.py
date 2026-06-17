
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:

    def __init__(self, driver):
        self.driver = driver

    def implicit_wait(self, timeout=10):
        self.driver.implicitly_wait(timeout)

    def explicit_wait(self, locator, condition="visible", timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        conditions = {
            "visible": EC.visibility_of_element_located(locator),
            "present": EC.presence_of_element_located(locator),
            "clickable": EC.element_to_be_clickable(locator),
            "invisibility": EC.invisibility_of_element_located(locator),
            "elements_visible": EC.presence_of_all_elements_located(locator)
        }

        return wait.until(conditions[condition])


    def fluent_wait(self, locator, condition="visible",
                    timeout=20, poll_frequency=1):
        wait = WebDriverWait(self.driver, timeout=timeout,
            poll_frequency=poll_frequency,ignored_exceptions=[NoSuchElementException])
        conditions = {
            "visible": EC.visibility_of_element_located(locator),
            "present": EC.presence_of_element_located(locator),
            "clickable": EC.element_to_be_clickable(locator),
            "invisibility": EC.invisibility_of_element_located(locator)
        }

        return wait.until(conditions[condition])

    def wait_for_dom_to_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")

    def wait_for_element_to_be_stale(self, element):
        return WebDriverWait(self.driver, 10).until(
            EC.staleness_of(element)
        )

    def wait_for_element_to_be_selected(self, element):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_selected(element)
        )

    def wait_for_element_located_to_be_selected(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_located_to_be_selected(locator)
        )

    def wait_for_element_selection_state(self, element, state=True):
        return WebDriverWait(self.driver, 10).until(
            EC.element_selection_state_to_be(element, state)
        )

    def wait_for_element_located_selection_state(self,locator,state=True):
        return WebDriverWait(self.driver,10).until(
            EC.element_located_selection_state_to_be(locator,state))
