import asyncio
from playwright.async_api import async_playwright

def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)#slow_mo=1000
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://coinpot.in/faucet")  # Replace with your actual URL
        print('got to coinpot')

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



r"""
C:\Users\drake\.conda\envs\tf\python.exe D:\Documents\github\Free-time-coding\playwrite\btc_async_4.0.py 
got to coinpot
Error processing link '': Unexpected token "" while parsing selector ""
Error processing link 'Features': Timeout 30000ms exceeded.
Error processing link 'User Benefits': Timeout 30000ms exceeded.
Error processing link 'Payment Proof': Timeout 30000ms exceeded.
Error processing link 'Statistics': Timeout 30000ms exceeded.
Error processing link 'FAQ': Timeout 30000ms exceeded.
Error processing link 'Contact Us': Timeout 30000ms exceeded.
Error processing link 'Login': Timeout 30000ms exceeded.
Error processing link 'Register': Timeout 30000ms exceeded.
Error processing link 'Register': Timeout 30000ms exceeded.
Error processing link 'Login': Timeout 30000ms exceeded.
Error processing link 'Visit FAQ': Timeout 30000ms exceeded.
Error processing link 'Submit a Ticket': Timeout 30000ms exceeded.
Error processing link 'Join Telegram': Timeout 30000ms exceeded.
Error processing link '': Unexpected token "" while parsing selector ""
Error processing link '': Unexpected token "" while parsing selector ""
Error processing link '': Unexpected token "" while parsing selector ""
Error processing link '': Unexpected token "" while parsing selector ""
Error processing link 'Telegram': Timeout 30000ms exceeded.
Error processing link 'Privacy Policy': Timeout 30000ms exceeded.
Error processing link 'Terms & Conditions': Unexpected token "&" while parsing selector "Terms & Conditions"
Error processing link 'Support': Timeout 30000ms exceeded.
Error processing link 'SHIB Faucet': Timeout 30000ms exceeded.
Error processing link 'Solana Faucet': Timeout 30000ms exceeded.
Error processing link 'DOGE Faucet': Timeout 30000ms exceeded.
Error processing link 'BNB Faucet': Timeout 30000ms exceeded.

Process finished with exit code 0

"""