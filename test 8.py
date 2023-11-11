from pathlib import Path

from selenium import webdriver
import time

# added driver to %path%
# (tf) PS C:\Users\drakeredwind01> pip show selenium
# Name: selenium
# Version: 4.14.0
# Summary: Python bindings for Selenium
# Home-page: https://github.com/SeleniumHQ/selenium/
# Author:
# Author-email:
# License: Apache 2.0
# Location: C:\Users\drakeredwind01\.conda\envs\tf\Lib\site-packages
# Requires: certifi, trio, trio-websocket, urllib3
# Required-by:

# Create a new Firefox driver

folder_path = Path("D:\documents\GitHub\Free time coding\_apps\chromedriver.exe")
driver = webdriver.Chrome()
# webdriver_service = service.Service('')
# webdriver_service.start()



# Load the first URL
driver.get("https://example.com")

# Wait for the page to load
time.sleep(3)

# Get all the open tabs
tabs = driver.window_handles

# Loop through the tabs
for tab in tabs:
    # Get the current URL
    current_url = driver.current_url

    # If the current URL is one of the three specific URLs, delete the tab
    if current_url == "https://www.google.com/" or current_url == "https://www.facebook.com/" or current_url == "https://www.reddit.com/":
        driver.switch_to.window(tab)
        driver.close()

# Wait for the script to finish executing
time.sleep(5)

# Close the driver
driver.quit()

















