"""
checkout_page.py
Handles checkout functionality.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from CapstoneProject.Pages.base_page import BasePage
from CapstoneProject.common import Config

class CheckoutPage(BasePage):
    """Page class for checkout functionality."""
    def fill_checkout_details(self, first_name, last_name, postal_code):
        """Fills checkout details."""
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, 'first-name')))
            self.driver.find_element(By.XPATH, Config.FIRST_NAME_FIELD).send_keys(first_name)
            self.driver.find_element(By.XPATH, Config.LAST_NAME_FIELD).send_keys(last_name)
            self.driver.find_element(By.XPATH, Config.ZIP_CODE_FIELD).send_keys(postal_code)
            self.driver.find_element(By.XPATH, Config.CONTINUE_BUTTON).click()
        except (TimeoutException, NoSuchElementException) as error:
            print(f"Error: {error}")

    def take_screenshot(self, file_name):
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_info')))
            self.driver.save_screenshot(file_name)
        except TimeoutException as e:
            print(f"Error: {e}")

    def verify_product_details(self, expected_details):
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item_name')))
            actual_details = [item.text for item in self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')]
            return actual_details == expected_details
        except TimeoutException as error:
            print(f"Error: {error}")
            return False

    def finish_checkout(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, 'finish')))
            self.driver.find_element(By.ID, 'finish').click()
        except TimeoutException as e:
            print(f"Error:{e}")

    def get_confirmation(self):
        self.confirmation_message = (By.CLASS_NAME, 'complete-header')
        return self.driver.find_element(*self.confirmation_message).text
