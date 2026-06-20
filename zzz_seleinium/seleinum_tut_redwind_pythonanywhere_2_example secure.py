

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from dotenv import load_dotenv
import os
import time

# pip install python-dotenv
load_dotenv(".env_test")
ADMIN_URL = os.getenv("DJANGO_ADMIN_URL")
USERNAME   = os.getenv("DJANGO_USERNAME")
PASSWORD   = os.getenv("DJANGO_PASSWORD")


options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

service = Service(executable_path="/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service, options=options)

# driver.get("https://www.ebay.com/sch/i.html?_nkw=graphics+card&_sacat=0&_from=R40&_trksid=p4439441.m570.l1311")
# driver.get("https://drakeredwind01.pythonanywhere.com")
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get(ADMIN_URL)


title = driver.title
print(title)




# time.sleep(3)

# Target the submit input inside Django admin's .submit-row div
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-row input[type='submit']")
#                                         <div class="submit-row">  <input type="submit" value="Log in">
is_enabled_button = submit_button.is_enabled()
print(f"Is the submit button enabled? {is_enabled_button}")



#username
text_box = driver.find_element(by=By.ID, value="id_username")
text_box.send_keys(USERNAME)


#password
text_box = driver.find_element(by=By.NAME, value="password")
text_box.send_keys(PASSWORD)




submit_button.click()


input("Press Enter to close...")

driver.quit()




'''
# Wait for page to load before finding elements
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "my-text")))


text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


text_box.send_keys("Selenium")


submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-row input[type='submit']")
#                                         <div class="submit-row">  <input type="submit" value="Log in">



────────────────────────────────────────────────────────────────────────────────
❯ for "random_python/seleinum_tut_redwind_pythonanywhere_1.py"
  for "<input type="text" name="username" autofocus="" autocapitalize="none"
  autocomplete="username" maxlength="150" required="" id="id_username">"
  help us select this box and imput the lower username. ~line 41

'''