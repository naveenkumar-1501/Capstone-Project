"""
test_checkout.py
Tests the checkout process.
"""

import pytest
import random
from CapstoneProject.Pages.check_out import CheckoutPage
from CapstoneProject.Pages.cart_page import CartPage
from CapstoneProject.Pages.inventory_page import InventoryPage
from CapstoneProject.common import Config
from CapstoneProject.utils.screenshot_helper import capture_screenshot
from CapstoneProject.Pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture(scope="function")
def add_products_to_cart(driver):
    """Add products to the cart and return product details."""
    driver.get(Config.URL)
    # Log in
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    # Ensure login success
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    # Choose 4 random products
    inventory_page = InventoryPage(driver)
    products = inventory_page.get_products()
    assert len(products) > 0, "No products found on the inventory page."
    random_products = random.sample(products, 4)
    # Add to cart
    for product in random_products:
        inventory_page.add_to_cart(product)
        print(f"Added to cart: {product.find_element(By.CLASS_NAME, 'inventory_item_name').text}")
    # Get the products added to the cart
    cart_page = CartPage(driver)
    cart_products = cart_page.get_cart_products()
    return cart_products

def test_checkout(driver, add_products_to_cart):
    """Tests the checkout flow."""
    driver.get(Config.URL)
    # Log in
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    # Go to cart
    wait = WebDriverWait(driver, 10)
    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, Config.CART)))
    cart_link.click()
    # Wait until the checkout button is visible and clickable
    try:
        checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Config.CHECK_OUT)))
        print("checkout button is clickable")
        checkout_button.click()
    except TimeoutException:
        print("Timeout occurred while waiting for the Checkout button to become clickable.")
        capture_screenshot(driver)  # Capture screenshot for debugging
        print("Page Source at failure:\n", driver.page_source)
        raise
    # Checkout Page steps
    checkout_page = CheckoutPage(driver)
    # Fill in checkout details
    checkout_page.fill_checkout_details("Tiffany", "Niven", "96718")
    # Capture screenshot before clicking the continue button
    capture_screenshot(driver)
    # Verify products on the checkout overview page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item_name')))
    # Finish the checkout process
    checkout_page.finish_checkout()
    # Assert if checkout completed successfully
    try:
        WebDriverWait(driver, 20).until(EC.url_contains("checkout-complete"))
    except TimeoutException:
        print("Checkout not completed within expected time.")
        capture_screenshot(driver)  # Capture screenshot for debugging
        raise
    assert "checkout-complete" in driver.current_url, "Checkout not completed!"
