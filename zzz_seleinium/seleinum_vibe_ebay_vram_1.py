from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import time

# =========================================
# CONFIG
# =========================================

SEARCH_QUERY = "RTX graphics card"

MAX_PRICE = 1000
CARDS_NEEDED = 4

# =========================================
# CHROME SETUP
# =========================================

options = Options()

# Keeps browser open
options.add_experimental_option("detach", True)

# Makes selenium less detectable
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# =========================================
# OPEN EBAY
# =========================================

# url = f"https://www.ebay.com/sch/i.html?_nkw={SEARCH_QUERY}"
url = f"zzz_seleinium/test_ebay_com/clean_ebay.html"

print("Opening:", url)

driver.get(url)

# =========================================
# WAIT FOR PAGE
# =========================================

wait = WebDriverWait(driver, 20)

wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "li.s-item")
    )
)

time.sleep(3)

# =========================================
# GET LISTINGS
# =========================================

items = driver.find_elements(
    By.CSS_SELECTOR,
    "li.s-item"
)

print(f"\nFound {len(items)} raw listings")

gpu_results = []

# =========================================
# HELPERS
# =========================================

def extract_price(text):

    match = re.search(r"\$([\d,]+\.?\d*)", text)

    if match:
        return float(match.group(1).replace(",", ""))

    return None


def extract_vram(title):

    title = title.upper()

    patterns = [
        r"(\d+)\s*GB",
        r"(\d+)\s*G\b",
    ]

    for pattern in patterns:

        match = re.search(pattern, title)

        if match:

            vram = int(match.group(1))

            if 2 <= vram <= 128:
                return vram

    return None


def suspicious(title):

    bad = [
        "BOX",
        "EMPTY",
        "PHOTO",
        "READ",
        "BROKEN",
        "FOR PARTS",
        "FAN",
        "COOLER",
        "HEATSINK",
    ]

    title = title.upper()

    return any(word in title for word in bad)

# =========================================
# PARSE LISTINGS
# =========================================

for item in items:

    try:

        title_el = item.find_element(
            By.CSS_SELECTOR,
            ".s-item__title"
        )

        title = title_el.text.strip()

        if not title:
            continue

        if suspicious(title):
            continue

        # Skip "Shop on eBay" fake item
        if "Shop on eBay" in title:
            continue

        price_el = item.find_element(
            By.CSS_SELECTOR,
            ".s-item__price"
        )

        price_text = price_el.text.strip()

        price = extract_price(price_text)

        if not price:
            continue

        if price > MAX_PRICE:
            continue

        vram = extract_vram(title)

        if not vram:
            continue

        link = item.find_element(
            By.CSS_SELECTOR,
            "a.s-item__link"
        ).get_attribute("href")

        score = vram / price

        gpu_results.append({
            "title": title,
            "price": price,
            "vram": vram,
            "score": score,
            "link": link
        })

        print(
            f"{vram}GB | "
            f"${price:.2f} | "
            f"{title}"
        )

    except Exception as e:
        pass

# =========================================
# SORT RESULTS
# =========================================

gpu_results.sort(
    key=lambda x: (
        x["score"],
        x["vram"]
    ),
    reverse=True
)

# =========================================
# RESULTS
# =========================================

print("\n" + "=" * 60)
print("BEST GPU DEALS")
print("=" * 60)

best = gpu_results[:CARDS_NEEDED]

if not best:

    print("\nNO GPU RESULTS FOUND\n")

else:

    for i, gpu in enumerate(best):

        print(f"\nGPU #{i+1}")

        print(f"VRAM:  {gpu['vram']}GB")

        print(f"PRICE: ${gpu['price']:.2f}")

        print(f"SCORE: {gpu['score']:.4f}")

        print(f"TITLE: {gpu['title']}")

        print(f"LINK:  {gpu['link']}")

        # Open tab
        driver.execute_script(
            f"window.open('{gpu['link']}', '_blank');"
        )

print("\nDONE")

input("\nPress ENTER to quit...")
