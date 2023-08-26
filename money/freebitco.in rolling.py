from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def auto_roll():

    browser = webdriver.Chrome("divers/operadriver_win64/operadriver.exe") # Your webdriver path
    browser.get("https://freebitco.in/")
    browser.implicitly_wait(30)

    # Try to close allow alert
    try:
        time.sleep(10)
        allow_btn = "(//div[@class='pushpad_deny_button'])[1]"
        browser.find_element_by_xpath(allow_btn).click()
    except:
        pass

    browser.find_element_by_class_name("login_menu_button").click()

    elem = browser.find_element_by_id("login_form_btc_address")
    elem.send_keys("Your Mail") # Your email or btc address
    elem = browser.find_element_by_id("login_form_password")
    elem.send_keys("Your Password") # Your password

    browser.find_element_by_id("login_button").click()

    #wait page and alert loading
    # Try to close allow alert
    try:
        time.sleep(10)
        allow_btn = "(//div[@class='pushpad_deny_button'])[1]"
        browser.find_element_by_xpath(allow_btn).click()
    except:
        pass

    # Scroll to buttom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    try:
        browser.find_element_by_id("free_play_form_button").click()
        print("Clicked!")
    except:
        browser.find_element_by_id("time_remaining")
        print("Need to wait.")

    time.sleep(2)
    browser.close()

    sched = BlockingScheduler()
    sched.add_job(auto_roll, 'interval', hours=1)
    sched.start()
if __name__ == '__main__':
    auto_roll()












'''
BROWSER             DOWNLOAD LOCATION
Opera               https://github.com/operasoftware/operachromiumdriver/releases
Firefox             https://github.com/mozilla/geckodriver/releases
Chrome              http://chromedriver.chromium.org/downloads
Internet Explorer   https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver
Microsoft Edge      https://blogs.windows.com/msedgedev/2015/07/23/bringing-automated-testing-to-microsoft-edge-through-webdriver/
'''







