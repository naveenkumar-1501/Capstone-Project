"""
test_logout.py
"""

from CapstoneProject.Pages.login_page import LoginPage
from CapstoneProject.Pages.inventory_page import InventoryPage
from CapstoneProject.common import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def test_logout(driver):
    """Tests logging out functionality."""
    # Navigate to the website
    driver.get(Config.URL)
    # Log in
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    # Ensure login is successful by checking if we are on the inventory page
    inventory_page = InventoryPage(driver)
    assert "inventory" in driver.current_url, "Login failed!"
    # Open the menu bar and click on logout
    inventory_page.click_element(Config.MENU_BAR)
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Config.LOGOUT_BUTTON)))
    # Ensure the logout button is visible and interactable
    assert logout_button.is_displayed() and logout_button.is_enabled(), "Logout button is not interactable!"
    # Click the logout button
    ActionChains(driver).move_to_element(logout_button).click().perform()
    # Verify logout was successful by checking that we're back on the login page
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, Config.USERNAME_FIELD)))
    assert driver.current_url == Config.URL, "Logout failed!"
