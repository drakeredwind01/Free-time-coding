import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.eveonlineships.com/eve-ship-database.php?es=Hobgoblin+I&ids=2454")
    # await expect(page.locator("div").filter(has_text="Hobgoblin I dronesCombat").nth(2)).to_be_visible()
    await page.is_visible('div.wrBoxw')
    html


    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
