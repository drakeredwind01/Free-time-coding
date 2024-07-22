import asyncio
from asyncio import timeout

from playwright.async_api import async_playwright
config = { timeout: 5000 }
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, timeout=1000)#slow_mo=1000
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.eveonlineships.com/eve-ship-database.php?es=Hobgoblin+I&ids=2454")        # Replace with your actual URL
        print('got to github security triage')

        # Get all link texts and store them in a list
        link_texts = await page.get_by_role("link").all_inner_texts()
        # this returns a list of strings

        # Iterate through each link text
        for text in link_texts:
            if text == '':
                continue

            try:
                # Build a dynamic locator for the link based on text
                link_locator = page.locator(f"text >> {text}")

                # Click the link (adjust click action if needed)
                await link_locator.click()

                # Download logic (add your specific download handling here)
                # ...

            except Exception as e:
                # Handle potential errors like invalid links or download failures
                print(f"Error processing link '{text}': {e}")

        # Close browser context and browser
        await page.close()
        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
