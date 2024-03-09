import asyncio
from playwright.async_api import async_playwright, Playwright
import time
# from ..config.config.py import username, password



async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()
    # Navigate to the website and perform actions
    await page.goto("https://coinpot.in/faucet")
    print('got to coinpot')
    texts=[]
    texts = await page.get_by_role("link").all_inner_texts()
    for urlnames in texts:
        print(urlnames +'\n')

    await page.locator('ms-auto btn-one').click()
    await page.locator('Login').click()


    page.screenshot(path="coin-farm.net/account/store")
    await page.locator('#log_email').fill('drakeredwind01@gmail.com')
    await page.locator('#log_email').fill('superpassword')


    # Keep the script running indefinitely to prevent browser closure
    while True:
        time.sleep(10)  # Check for termination every 10 seconds

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())


'''
ask jeremy
    if page.locator('ms-auto btn-one')==True
        print('found ms-auto btn-one')


'''

'''
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
'''