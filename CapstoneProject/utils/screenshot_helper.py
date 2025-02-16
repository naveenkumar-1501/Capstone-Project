"""
screenshot_helper.py
Utility for capturing screenshots.
"""
import os
from datetime import datetime

def capture_screenshot(driver, screenshot_dir="screenshots"):
    """Captures a screenshot."""
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
    driver.save_screenshot(path)
    return path
