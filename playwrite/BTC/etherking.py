from playwright.sync_api import Playwright, sync_playwright, expect
import keyboard
import time
from wait_for import speak_and_print_etherking
import BTC_C

def wait_for_help():
    print(f"flease hit shift+q after solving")
    if keyboard.is_pressed('shift+q'):
        print(f"continuing script")
        pass

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://etherking.io/login.php")
    page.locator("#user_email").click()
    page.locator("#user_email").fill(BTC_C.etherking_u)
    page.locator("#password").click()
    page.locator("#password").fill(BTC_C.etherking_p)
    page.frame_locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]").get_by_label("hCaptcha checkbox with text '").click()
    wait_for_help()
    page.get_by_role("button", name="Login").click()
    page.locator("#main_menu").get_by_role("link", name="Faucet").click()
    page.frame_locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]").get_by_label("hCaptcha checkbox with text '").click()
    wait_for_help()
    page.get_by_role("button", name="Free Spins:").click()
    print(f"trying click Free Spins 1")
    time.sleep(10)
    page.get_by_role("button", name="Free Spins:").click()
    print(f"trying click Free Spins 2")
    time.sleep(10)
    page.get_by_role("button", name="Free Spins:").click()
    print(f"trying click Free Spins 3")
    time.sleep(10)
    page.get_by_role("button", name="Free Spins:").click()
    print(f"trying click Free Spins 4")
    time.sleep(10)
    page.get_by_role("button", name="Free Spins:").click()
    print(f"trying click Free Spins 5")
    time.sleep(10)
    page.get_by_role("button", name="Free Spins:").click()
    print(f"trying click Free Spins 6")
    time.sleep(10)
    page.get_by_role("button", name="Free Spins:").click()
    print(f"trying click Free Spins 7")
    print(f"waiting 1 hour before running speak_and_print_etherking")
    time.sleep(3600)
    speak_and_print_etherking()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
