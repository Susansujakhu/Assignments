from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_clickable(self, locator):
        """
        Wait until the element is clickable.
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_visible(self, locator):
        """
        Wait until the element is visible.
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_present(self, locator):
        """
        Wait until the element is present in the DOM.
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_text_in_element(self, locator, text):
        """
        Wait until the given text is present in the element.
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def scroll_into_view(self, locator):
        """
        Scroll to the element making it visible
        """
        self.driver.execute_script(
            "window.scrollTo(0, arguments[0].offsetTop);", locator)
