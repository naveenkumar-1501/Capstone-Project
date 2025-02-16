"""
login_page.py
Handles login functionality.
"""
import json
from selenium.webdriver.support import expected_conditions as EC
from CapstoneProject.Pages.base_page import BasePage
from CapstoneProject.common import Config

class LoginPage(BasePage):
    """Page class for login functionality."""
    def login(self, username, password):
        """Logs in with provided credentials."""
        self.input_text(Config.USERNAME_FIELD, username)
        self.input_text(Config.PASSWORD_FIELD, password)
        self.click_element(Config.LOGIN_BUTTON)

    def get_error_message(self):
        """Retrieves the error message displayed on login failure."""
        return self.get_text(Config.ERROR_MESSAGE)

    def login_using_cookies(self, driver):
        """Logs in using stored cookies from cookies.json."""
        self.driver.get("https://www.saucedemo.com/")
        try:
            with open("cookies.json", "r") as file:
                cookies = json.load(file)
                for cookie in cookies:
                    if "sameSite" in cookie and cookie["sameSite"] is None:
                        cookie["sameSite"] = "Lax"
                    self.driver.add_cookie(cookie)
            print("Cookies add successfully!")
            self.driver.get("https://www.saucedemo.com/inventory.html")
            self.wait.until(EC.url_contains("inventory"))
            print("Logged in using cookies!")
        except Exception as error:
            print(f"Error logging in using cookies: {error}")
