"""
test_cart_button.py
"""
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CapstoneProject.Pages.login_page import LoginPage
from CapstoneProject.Pages.cart_page import CartPage
from CapstoneProject.common import Config

def test_cart_button_visibility(driver):
        """Check whether the cart button is visible"""
        driver.get(Config.URL)
        # Log in
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, Config.CART)))
        # Check cart button visibility
        cart_page = CartPage(driver)
        print("Checking if the cart button is visible on the homepage.")
        try:
                assert cart_page.is_cart_button_visible(), "Cart button is not visible on the homepage."
        except AssertionError as error:
                with open("page_source.html", "w", encoding="utf-8") as file:
                        file.write(driver.page_source)
                cart_button = driver.find_element(By.XPATH, Config.CART)
                print("Is Displayed:", cart_button.is_displayed())
                raise error
