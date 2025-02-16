"""
test_login.py
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from CapstoneProject.Pages.login_page import LoginPage
from CapstoneProject.common import Config
import csv
import os

def load_credentials(filename):
    """Loads credentials from a CSV file."""
    if not os.path.exists(filename):
        pytest.fail(f"CSV file '{filename}' not found.")
    try:
        with open(filename, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            print("Header:", reader.fieldnames)
            required_headers = {"username", "password", "is_valid"}
            if not reader.fieldnames or not required_headers.issubset(reader.fieldnames):
                pytest.fail(f"CSV file '{filename}' must have 'username', 'password', and 'is_valid' columns.")
            return [
                (row["username"].strip(), row["password"].strip(), row["is_valid"].strip().lower() == "true")
                for row in reader
            ]
    except Exception as error:
        pytest.fail(f"Error reading CSV file '{filename}': {error}")

@pytest.mark.parametrize("username, password, is_valid", load_credentials("data/credentials.csv"))
def test_login(driver, username, password, is_valid):
    """Tests login with valid and invalid credentials."""
    driver.get(Config.URL)
    login_page = LoginPage(driver)
    login_page.login(username, password)
    try:
        # Wait for error message or successful login
        WebDriverWait(driver, 5).until(lambda d: d.find_elements(By.XPATH, Config.ERROR_MESSAGE) or "inventory" in d.current_url)
        if is_valid:
            # Valid login should navigate to inventory page
            assert "inventory" in driver.current_url, f"Valid login failed for {username}."
        else:
            # Invalid login should show error message
            error_message = driver.find_element(By.XPATH, Config.ERROR_MESSAGE).text.strip()
            expected_message = (
                "Epic sadface: Sorry, this user has been locked out."
                if username == "locked_out_user"
                else "Epic sadface: Username and password do not match any user in this service"
            )
            assert error_message == expected_message, f"Unexpected error message for {username}: {error_message}"
    except TimeoutException:
        pytest.fail(
            f"Timeout occurred while testing login for {username}. Expected login status: {'valid' if is_valid else 'invalid'}.")

def test_login_using_cookies(driver):
    """Test login using stored cookies from cookies.json."""
    login_page = LoginPage(driver)
    login_page.login_using_cookies(driver)
    assert "inventory" in driver.current_url, "Login using cookies failed"