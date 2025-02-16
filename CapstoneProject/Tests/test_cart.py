"""
test_cart.py
"""

import pytest
import random
from CapstoneProject.Pages.cart_page import CartPage
from CapstoneProject.Pages.inventory_page import InventoryPage
from CapstoneProject.common import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from CapstoneProject.Pages.login_page import LoginPage

def test_cart_functionality(driver):
    """Tests the cart functionality."""
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
    # Print the products added to the cart
    print("Products added to the cart:")
    for product in random_products:
        name = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
        print(name)

def test_verify_product_added_to_cart(driver):
    driver.get(Config.URL)
    # Log in
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)
    # Ensure at least one product is visible before proceeding
    inventory_page = InventoryPage(driver)
    products = inventory_page.get_products()
    assert len(products) > 0, "No products available to add to cart."
    # Add products to cart
    random_products = random.sample(products, 4)
    for product in random_products:
        inventory_page.add_to_cart(product)
    # Ensure the cart badge updates
    try:
        cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        print(f"Cart badge count: {cart_badge.text}")
        assert int(cart_badge.text) == 4, f"Expected 4 items in cart, but got {cart_badge.text}"
    except TimeoutException:
        print("Cart badge not found. Products may not have been added.")
    # Navigate to cart
    cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, Config.CART)))
    cart_link.click()
    cart_page = CartPage(driver)
    # Wait for the cart items to load
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    except TimeoutException:
        print("Timeout while waiting for cart items to load.")
        # Capture screenshot and page source for debugging
        driver.save_screenshot("cart_page_screenshot.png")
        with open("cart_page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        raise
    # Fetch and print the cart items for debugging
    cart_products = cart_page.get_cart_products()
    print("Cart products:")
    for product in cart_products:
        print(product.text)
    cart_product_count = len(cart_products)
    print(f"Cart products count: {cart_product_count}")
    assert cart_product_count == 4, f"Expected 4 products in cart, but got {cart_product_count}"
    # Fetch product details
    product_details = [product.text for product in cart_products]
    # Print product details
    print("Product details in the cart:")
    for detail in product_details:
        print(detail)
