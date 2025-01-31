import asyncio
import time
from playwright.async_api import async_playwright, expect
import keyboard
import BTC_C
from playwrite.BTC import wait_for
from wait_for import speak_and_print_etherking, etherking_timer

# Async function to wait for the user to press 'shift+q' to continue
async def wait_for_help():
    start_time = time.time()
    print(f"Please hit shift+q after solving the captcha.")
    while time.time() - start_time < 30:
        if keyboard.is_pressed('shift+q'):
            print(f"Continuing script.")
            break

# Function to handle login and faucet task in one browser window
async def login_and_faucet(browser):
    try:
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://etherking.io/login.php")

        # Login process
        await page.locator("#user_email").click()
        await page.locator("#user_email").fill(BTC_C.etherking_u)
        await page.locator("#password").click()
        await page.locator("#password").fill(BTC_C.etherking_p)
        await page.frame_locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]").get_by_label("hCaptcha checkbox with text '").click()
        await wait_for_help()
        await page.get_by_role("button", name="Login").click()

        # Navigate to Faucet and handle captcha
        await page.locator("#main_menu").get_by_role("link", name="Faucet").click()
        await page.frame_locator("iframe[title=\"Widget containing checkbox for hCaptcha security challenge\"]").get_by_label("hCaptcha checkbox with text '").click()
        await wait_for_help()

        # Perform the Free Spins action
        await page.get_by_role("button", name="Free Spins:").click()

        # Wait and then call speak_and_print_etherking after 1 hour
        await wait_for.etherking_timer()
        print(f"Waiting 1 hour before running speak_and_print_etherking")
        await asyncio.sleep(3600)  # Use asyncio.sleep for async wait
        await speak_and_print_etherking()

        await context.close()  # Close the context (this closes all pages within it)
    except Exception as e:
        print(f"An error occurred in login_and_faucet: {e}")

# Another function to perform a different task in another window (can be extended to other tasks)
async def another_task_in_browser(browser):
    try:
        context = await browser.new_context()
        page = await context.new_page()

        # Example task: simply navigate to a page and wait for 10 seconds
        await page.goto("https://example.com")
        await asyncio.sleep(10)

        print("Finished another task in the second browser window.")
        await context.close()  # Close the context
    except Exception as e:
        print(f"An error occurred in another_task_in_browser: {e}")

# Main function to launch the browsers and run tasks concurrently
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        # Run multiple tasks concurrently (using asyncio.gather)
        await asyncio.gather(
            login_and_faucet(browser),  # Perform login and faucet task
            another_task_in_browser(browser)  # Perform another task in a second window
        )

        await browser.close()  # Close the browser once all tasks are done

# Run the main function
asyncio.run(main())
