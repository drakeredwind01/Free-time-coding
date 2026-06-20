

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

# driver.get("https://www.ebay.com/sch/i.html?_nkw=graphics+card&_sacat=0&_from=R40&_trksid=p4439441.m570.l1311")
# driver.get("https://drakeredwind01.pythonanywhere.com")
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


title = driver.title
print(title)

# Wait for page to load before finding elements
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "my-text")))

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

time.sleep(3)

text_box.send_keys("Selenium")


# message = driver.find_element(by=By.ID, value="message")
# text = message.text
# print(text)


# is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()

# CLASS_NAME doesn't support multiple classes — use CSS_SELECTOR with dot notation instead
is_enabled_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").is_enabled()
print(f"Is the submit button enabled? {is_enabled_button}")


input("Press Enter to close...")



submit_button.click()


input("Press Enter to close...")

driver.quit()
