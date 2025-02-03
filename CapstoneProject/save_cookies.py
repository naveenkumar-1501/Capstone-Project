"""
save_cookies.py
"""

import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function to log in and save cookies
def login_and_save_cookies(driver):
    """Login in save cookies"""
    driver.get("https://www.saucedemo.com/")  # Navigate to login page
    # Locate login elements and enter credentials
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("secret_sauce")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(Keys.RETURN)# Press Enter
    # Wait for login to complete by checking for the inventory page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inventory_container")))
    # Save cookies
    cookies = driver.get_cookies()
    with open("cookies.json", "w") as file:
        json.dump(cookies, file)
    print("Cookies saved successfully!")

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        login_and_save_cookies(driver)
    finally:
        driver.quit()