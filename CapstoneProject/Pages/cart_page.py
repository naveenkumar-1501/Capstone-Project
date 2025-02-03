"""
cart_page.py
Handles cart functionality.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CapstoneProject.Pages.base_page import BasePage
from CapstoneProject.common import Config

class CartPage(BasePage):
    def is_cart_button_visible(self):
        """Verify if cart button is visible"""
        try:
            cart_button = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, Config.CART)))
            return cart_button.is_displayed()
        except Exception as error:
            print(f"Error in checking cart button visibility: {error}")
            return

    def get_cart_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

