from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("redwind01.com")