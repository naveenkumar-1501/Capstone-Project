"""
test_inventory
"""

import pytest
from CapstoneProject.Pages.inventory_page import InventoryPage
from CapstoneProject.common import Config
from CapstoneProject.Pages.login_page import LoginPage

def test_random_products(driver):
    """Tests selecting and validating four random products."""
    driver.get(Config.URL)
    # Log in
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    random_products = inventory_page.get_random_products()
    product_details = set()
    for name, price in random_products:
        assert name is not None
        assert price is not None
        product_details.add((name, price)) # Add product details to the set
        for name, price in product_details:
           print(f"Product: {name}, Price:{price}")
