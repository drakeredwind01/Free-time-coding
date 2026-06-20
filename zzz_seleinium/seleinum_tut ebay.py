

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

import time


options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

service = Service(executable_path="/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.ebay.com/sch/i.html?_nkw=graphics+card&_sacat=0&_from=R40&_trksid=p4439441.m570.l1311")
# driver.get("https://drakeredwind01.pythonanywhere.com")
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")


title = driver.title
print(title)

input("Solve any CAPTCHA in the browser, then press Enter to continue...")

# Wait for eBay's search box to load (up to 30s to allow manual CAPTCHA solving)
text_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "gh-ac")))

print(f"Search box found: {text_box}")



# Wait for the first listing link to be clickable, then click it
xpath = "(//a[contains(@href, '/itm/')])[1]"
element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath)))
element.click()
print("Clicked first listing.")






input("Press Enter to close...")

driver.quit()
