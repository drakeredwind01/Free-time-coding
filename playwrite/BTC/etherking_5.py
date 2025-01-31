'''etherking_5.py'''
from playwright.sync_api import Playwright, sync_playwright, expect
import keyboard
import time

from playwrite.BTC import wait_for
from wait_for import speak_and_print_etherking, etherking_timer
import BTC_C
'''
look up os environ call
use os for codes in .env 
look up .env
remove credentials to source controls
look up decorator
'''

def wait_for_help(): # Jorge help
    start_time = time.time()
    print(f"Please hit shift+q after solving the captcha.")
    start_time = time.time()
    while time.time() - start_time < 30:  # wait for 30 seconds
        if keyboard.is_pressed('shift+q'):
            print(f"Continuing script.")
            break

# def wait_for_help():
#     print(f"Please hit shift+q after solving the captcha.")
#     if keyboard.is_pressed('shift+q'):
#         print(f"Continuing script.")
#         pass

# def wait_for_help(): # Jorge help
#     print(f"Please hit shift+q after solving the captcha.")
#     while True:
#         if keyboard.is_pressed('shift+q'):
#             print(f"Continuing script.")
#             break
#         else:
#             break

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://etherking.io/login.php")

    # Login section
    page.locator("#user_email").click()
    page.locator("#user_email").fill(BTC_C.etherking_u)
    page.locator("#password").click()
    page.locator("#password").fill(BTC_C.etherking_p)
    page.frame_locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]").get_by_label("hCaptcha checkbox with text '").click()
    wait_for_help()
    page.get_by_role("button", name="Login").click()

    # Navigate to Faucet and handle captcha (assuming one per login session)
    page.locator("#main_menu").get_by_role("link", name="Faucet").click()
    page.frame_locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]").get_by_label("hCaptcha checkbox with text '").click()
    wait_for_help()

    # Free Spins Loop with error handling for "Free Spins:" button
    free_spin_still_there = True
    # for i in range(10) and free_spin_still_there = True:
    page.get_by_role("button", name="Free Spins:").click()
    # Wait and call speak_and_print_etherking
    wait_for.etherking_timer()
    print(f"Waiting 1 hour before running speak_and_print_etherking")
    time.sleep(3600)
    speak_and_print_etherking()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)