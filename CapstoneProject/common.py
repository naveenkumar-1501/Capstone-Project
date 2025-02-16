"""
common.py
common configuration for web application
"""
class Config:
    """Class to hold constants and configuration details."""
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = "//input[@id= 'user-name']"
    PASSWORD_FIELD = "//input[@id= 'password']"
    LOGIN_BUTTON = "//input[@id= 'login-button']"
    ERROR_MESSAGE = "//h3[@data-test='error']"
    ADD_TO_CART = "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button"
    CART = "//a[@class = 'shopping_cart_link']"
    CHECK_OUT = "//button[@id='checkout']"
    FIRST_NAME_FIELD = "//input[@id='first-name']"
    LAST_NAME_FIELD = "//input[@id='last-name']"
    ZIP_CODE_FIELD = "//input[@id='postal-code']"
    CONTINUE_BUTTON = "//input[@id='continue']"
    FINISH_BUTTON = "//button[@id='finish']"
    MENU_BAR = "//button[@id='react-burger-menu-btn']"
    LOGOUT_BUTTON = "//a[@id='logout_sidebar_link']"
    DASHBOARD_ELEMENT = "//div[@class='inventory_list']"


