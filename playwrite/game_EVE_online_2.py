'''playwright codegen "https://www.eveonlineships.com/eve-ship-database.php?es=Hobgoblin+I&ids=2454"
'''
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.eveonlineships.com/eve-ship-database.php?es=Hobgoblin+I")
    page.goto("https://www.eveonlineships.com/eve-ship-database.php?es=Hobgoblin+I&ids=2454")
    expect(page.get_by_role("heading", name="Hobgoblin I", exact=True)).to_be_visible()
    base_price = expect(page.get_by_text("Base price: 2,500 ISK")).to_be_visible()
    Shield = expect(page.get_by_role("cell", name="Shield:")).to_be_visible()
    expect(page.get_by_role("cell", name="90")).to_be_visible()
    expect(page.get_by_role("cell", name="50")).to_be_visible()
    expect(page.get_by_role("cell", name="90")).to_be_visible()
    expect(page.get_by_role("cell", name="200")).to_be_visible()
    expect(page.get_by_text("Mass: 3000 kg")).to_be_visible()
    expect(page.get_by_text("Maximum velocity:")).to_be_visible()
    expect(page.get_by_text("Orbit Velocity 660")).to_be_visible()
    expect(page.get_by_text("EM damage 0")).to_be_visible()
    expect(page.get_by_text("Explosive damage 0")).to_be_visible()
    expect(page.get_by_text("Kinetic damage 0")).to_be_visible()
    expect(page.get_by_text("Thermal damage 20")).to_be_visible()
    expect(page.get_by_text("Accuracy falloff 2000")).to_be_visible()
    expect(page.get_by_text("Turret Tracking 1.815")).to_be_visible()
    expect(page.get_by_text("Rate of fire 4000")).to_be_visible()
    expect(page.get_by_text("Optimal Range 2100")).to_be_visible()
    print(f"{base_price}")
    print(f"{Shield}")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
