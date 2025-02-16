"""
inventory_page.py
"""

import random
from CapstoneProject.Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def get_random_products(self, count = 4):
        self.product_locators = (By. CLASS_NAME, 'inventory_item')
        products = self.driver.find_elements(*self.product_locators)
        selected_products = random.sample(products, count)
        product_details = []
        for product in selected_products:
            name = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = product.find_element(By.CLASS_NAME, 'inventory_item_price').text
            product_details.append((name, price))
        return product_details

    def get_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def add_to_cart(self, product):
        product.find_element(By.CLASS_NAME, "btn_inventory").click()

