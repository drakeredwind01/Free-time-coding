'''
scrapfly.io/blog/web-scraping-with-selenium-and-python/
github.com/natalyaburmistrova91/GeekBrains_Parsing
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

# Disallow list
disallowed_urls = ["https://www.facebook.com", "https://www.youtube.com"]

# Open a new tab
driver.execute_script("window.open();")

# Check the URL of the new tab
new_tab_url = driver.window_handles[-1]
driver.switch_to.window(new_tab_url)
current_url = driver.current_url

# If the URL is on the disallow list, close the tab
if current_url in disallowed_urls:
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

print("Tabs:", len(driver.window_handles))
