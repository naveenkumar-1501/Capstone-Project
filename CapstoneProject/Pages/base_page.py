"""
base_page,py

BasePage class includes common methods like find_element, click, send_keys
"""

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    """Base class for all pages to share common functions."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait for elements for up to 10 seconds

    def find_element(self, xpath: str):
        """Finds a web element using the provided XPath."""
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def find_elements(self, locator_type: str, locator: str):
        """Finds multiple elements using the provided locator."""
        if locator_type == "xpath":
            return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
        elif locator_type == "css selector":
            return self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        else:
            raise ValueError("Unsupported locator type.")

    def click_element(self, xpath: str) -> None:
        """Clicks on a given element."""
        self.find_element(xpath).click()

    def input_text(self, xpath: str, text: str) -> None:
        """Inputs text into a field."""
        element = self.find_element(xpath)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Gets the text of an element specified by the locator."""
        try:
            element = self.driver.find_element(*locator)
            return element.text
        except Exception as error:
            print(f"Error retrieving text: {error}")
            return None

    def is_element_visible(self, locator):
        """Checks if an element is visible on the page."""
        try:
           element = self.driver.find_element(*locator)
           return element.is_displayed()
        except Exception:
            return False
