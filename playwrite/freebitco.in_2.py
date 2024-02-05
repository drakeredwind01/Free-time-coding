from playwright.sync_api import sync_playwright
import time

# Initiate Playwright context outside the 'with' block
p = sync_playwright().start()

try:
    # Launch Opera browser
    browser = p.chromium.launch(headless=False, slow_mo=1000)

    # Navigate to the website and perform actions
    page = browser.new_page()
    page.goto("https://freebitco.in/?op=home")
    page.fill('input#signup_form_email', 'drakeredwind01@gmail.com')      # id = "signup_form_email"
    page.fill('input#signup_form_password', 'superpassword')      # id="signup_form_password"
    time.sleep(5)
    # page.locator(' ALLOW ').click()
    print('will try to hit allow')
    # page.locator('class=pushpad_allow_button').get_by_text('Click me').click()
    page.locator('text=ALLOW').click()
    print('try to hit allow')
    # Wait for actions to complete
    time.sleep(5)

    # Keep the script running indefinitely to prevent browser closure
    while True:
        time.sleep(10)  # Check for termination every 10 seconds

finally:
    while True:
        time.sleep(10)  # Check for termination every 10 seconds

'''
finally:
    # Ensure Playwright context is closed even if exceptions occur
    p.stop()
'''

