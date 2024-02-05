from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch a new Opera browser context using the existing user data directory
    browser = p.chromium.launch(headless=False, slow_mo=1000)

    # Navigate to the website
    page = browser.new_page()
    page.goto("https://freebitco.in/?op=home")

    # Click the checkbox element
    checkbox = page.query_selector("#checkbox")
    checkbox.click()

    # Click the button
    button = page.query_selector("#free_play_form_button")
    button.click()

    # Wait for some time to allow actions to complete (adjust as needed)
    time.sleep(5)

    # Close the browser
    # browser.close()
