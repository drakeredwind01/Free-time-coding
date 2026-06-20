import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =========================================================
# DRIVER FIXTURE
# =========================================================

@pytest.fixture
def driver():

    options = Options()

    # Keeps browser open after crash
    options.add_experimental_option(
        "detach",
        True
    )

    # More stable on Linux
    options.add_argument("--no-sandbox")

    options.add_argument(
        "--disable-dev-shm-usage"
    )

    # Anti detection
    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    # OPTIONAL:
    # use your real browser profile
    #
    # options.add_argument(
    #     "--user-data-dir=/home/drake/.config/google-chrome"
    # )

    driver = webdriver.Chrome(
        options=options
    )

    yield driver

    try:
        driver.quit()
    except:
        pass

# =========================================================
# TEST CHROME OPENS
# =========================================================

def test_chrome_launch(driver):

    driver.get("https://example.com")

    assert "Example" in driver.title

# =========================================================
# TEST SESSION STAYS ALIVE
# =========================================================

def test_session_alive(driver):

    driver.get("https://google.com")

    time.sleep(3)

    assert driver.current_url.startswith(
        "https://"
    )

# =========================================================
# TEST EBAY LOADS
# =========================================================

def test_ebay_homepage(driver):

    driver.get("https://www.ebay.com")

    assert "eBay" in driver.title

# =========================================================
# TEST SEARCH WORKS
# =========================================================

def test_ebay_search(driver):

    url = (
        "https://www.ebay.com/"
        "sch/i.html?_nkw=rtx+graphics+card"
    )

    driver.get(url)

    assert "rtx" in driver.current_url.lower()

# =========================================================
# TEST LISTINGS EXIST
# =========================================================

def test_ebay_listings_exist(driver):

    url = (
        "https://www.ebay.com/"
        "sch/i.html?_nkw=rtx+graphics+card"
    )

    driver.get(url)

    wait = WebDriverWait(
        driver,
        20
    )

    listings = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li.s-item")
        )
    )

    print(
        f"\nFOUND {len(listings)} LISTINGS"
    )

    assert len(listings) > 5

# =========================================================
# TEST TITLES EXIST
# =========================================================

def test_listing_titles(driver):

    url = (
        "https://www.ebay.com/"
        "sch/i.html?_nkw=rtx+graphics+card"
    )

    driver.get(url)

    wait = WebDriverWait(
        driver,
        20
    )

    listings = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li.s-item")
        )
    )

    titles_found = 0

    for item in listings:

        try:

            title = item.find_element(
                By.CSS_SELECTOR,
                ".s-item__title"
            ).text.strip()

            if title:
                titles_found += 1

        except:
            pass

    print(
        f"\nFOUND {titles_found} TITLES"
    )

    assert titles_found > 5

# =========================================================
# TEST BOT DETECTION
# =========================================================

def test_not_blocked(driver):

    url = (
        "https://www.ebay.com/"
        "sch/i.html?_nkw=rtx+graphics+card"
    )

    driver.get(url)

    source = driver.page_source.lower()

    blocked_words = [
        "captcha",
        "robot",
        "verify you are human",
        "access denied",
    ]

    blocked = any(
        word in source
        for word in blocked_words
    )

    assert blocked is False

# =========================================================
# DEBUG HTML DUMP
# =========================================================

def test_dump_html(driver):

    url = (
        "https://www.ebay.com/"
        "sch/i.html?_nkw=rtx+graphics+card"
    )

    driver.get(url)

    html = driver.page_source

    with open(
        "debug_ebay.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    assert len(html) > 1000
