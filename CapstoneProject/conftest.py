"""
conftest.py

It is used to manage the WebDriver Setup and Teardown

Centralizes WebDriver Setup making it reusable across tests
"""

import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and teardown WebDriver."""
    logging.info("Initialing WebDriver")
    driver = None
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()  # Maximize the window for better visibility
        yield driver  # Yielding driver to the test function
    except Exception as error:
        logging.error("Failed to initialize WebDriver", exc_info=True)
        pytest.fail(f"WebDriver setup failed: {error}")
    finally:
        if driver:
            logging.info("Quitting WebDriver")
            driver.quit()