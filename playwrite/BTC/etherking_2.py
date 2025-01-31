from playwright.sync_api import Playwright, sync_playwright, expect
import keyboard
import time
from wait_for import speak_and_print_etherking
import BTC_C
'''
look up os environ call
'''




def wait_for_help():
    print(f"Please hit shift+q after solving the captcha.")
    if keyboard.is_pressed('shift+q'):
        print(f"Continuing script.")
        pass

def wait_for_help():
    print(f"Please hit shift+q after solving the captcha.")
    while True:
        if keyboard.is_pressed('shift+q'):
            print(f"Continuing script.")
            break

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
    i = 0
    while free_spin_still_there:
        if page.get_by_role("button", name="Free Spins:").click():
            i += 1
            print(f"found it running again #{i}")
            return  # Found the image, exit the function
        else:
            time.sleep(1)  # Wait for 1 second before retrying
            print(f"Failed to find after '{i}' tries.")
    all_attempts_successful = True  # Flag to track success
    success = False
    for attempt in range(1, 8):  # Loop 7 times for Free Spins attempts
        try:
            page.get_by_role("button", name="Free Spins:").click()
            print(f"Attempting Free Spins click #{attempt}")
        except (playwright.errors.ElementNotFound, playwright.errors.TimeoutError):
            print(f"Free Spins button not found on attempt #{attempt}.")
            all_attempts_successful = False  # Mark unsuccessful attempt
        time.sleep(10)  # Adjust sleep time as needed

    # Informative message based on attempt success
    if all_attempts_successful:
        print(f"Successfully attempted all 7 Free Spins!")
    else:
        print(f"Free Spins button might not be available or might have timed out during some attempts.")

    # Wait and call speak_and_print_etherking
    print(f"Waiting 1 hour before running speak_and_print_etherking")
    time.sleep(3600)
    speak_and_print_etherking()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)