from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from dataclasses import dataclass, field
from collections import defaultdict
import re
import time
import json

# =========================================
# CONFIG
# =========================================

PAGES_PER_QUERY  = 3       # eBay pages to scrape per search query
MIN_PRICE        = 50.0    # below this = scam
MAX_PRICE        = 3000.0  # above this = skip for value ranking
MIN_VRAM_GB      = 8       # anything less is useless for LLM
CARDS_NEEDED     = 4       # building a 4-GPU tower

# GPU models and their known VRAM — checked before regex so 3080 (10GB) vs 3080 12GB is correct
KNOWN_VRAM: dict[str, int] = {
    "rtx 4090":          24,
    "rtx 4080 super":    16,
    "rtx 4080":          16,
    "rtx 4070 ti super": 16,
    "rtx 4070 ti":       12,
    "rtx 4070 super":    12,
    "rtx 4070":          12,
    "rtx 4060 ti 16gb":  16,
    "rtx 4060 ti":        8,
    "rtx 4060":           8,
    "rtx 3090 ti":       24,
    "rtx 3090":          24,
    "rtx 3080 ti":       12,
    "rtx 3080 12gb":     12,
    "rtx 3080":          10,
    "rtx 3070 ti":        8,
    "rtx 3070":           8,
    "rtx 3060 ti":        8,
    "rtx 3060":          12,
    "rtx 2080 ti":       11,
    "rtx 2080 super":     8,
    "rtx 2080":           8,
    "rtx 2070 super":     8,
    "rtx 2070":           8,
    "rtx 2060 super":     8,
    "rtx 2060":           6,
    "rx 7900 xtx":       24,
    "rx 7900 xt":        20,
    "rx 7800 xt":        16,
    "rx 6900 xt":        16,
    "rx 6800 xt":        16,
    "rx 6800":           16,
    "rx 6700 xt":        12,
    "rx 6600 xt":         8,
    "rx 6600":            8,
    "a100":              80,
    "a40":               48,
    "a30":               24,
    "a10":               24,
    "v100":              32,
    "p100":              16,
}

# Title substrings that mean the listing is junk/not an actual GPU
JUNK_KEYWORDS = [
    "lot of", "for parts", "parts only", "broken", "non working",
    "not working", "as is", "untested", "defective", "damaged",
    "salvage", "spares", "repair", "empty box", "box only",
    "photo only", "fan only", "cooler only", "heatsink",
    "mining edition", "bios chip",
]

# Search queries sent to eBay — cast a wide net across price tiers
SEARCH_QUERIES = [
    "nvidia rtx 3090 graphics card",
    "nvidia rtx 3080 graphics card",
    "nvidia rtx 4090 graphics card",
    "nvidia rtx 4070 graphics card",
    "amd rx 6900 xt graphics card",
    "amd rx 7900 xt graphics card",
]

# =========================================
# DATA MODEL
# =========================================

@dataclass
class GPUListing:
    title:     str
    price:     float
    shipping:  float
    vram_gb:   int
    condition: str
    url:       str
    model_key: str = field(init=False)
    vpd:       float = field(init=False)   # VRAM per dollar (total cost)

    def __post_init__(self):
        self.model_key = _normalize_model(self.title)
        total = self.price + self.shipping
        self.vpd = self.vram_gb / total if total > 0 else 0.0

# =========================================
# HELPERS
# =========================================

def _normalize_model(title: str) -> str:
    t = title.lower()
    # Longest match first so "rtx 3080 12gb" beats "rtx 3080"
    for model in sorted(KNOWN_VRAM, key=len, reverse=True):
        if model in t:
            return model
    # Fallback: grab RTX/GTX/RX + number
    m = re.search(r"(rtx|gtx|rx|arc)\s*(\d{3,4}(?:\s*(?:ti|xt|super|xtx))?)", t)
    if m:
        return f"{m.group(1)} {m.group(2).strip()}"
    return "unknown"


def _extract_vram(title: str) -> int | None:
    t = title.lower()
    for model in sorted(KNOWN_VRAM, key=len, reverse=True):
        if model in t:
            return KNOWN_VRAM[model]
    # Regex: "16GB GDDR6X", "24 GB VRAM", "24GB"
    for pat in [
        r"(\d+)\s*gb\s*(?:gddr\d+[x]?|hbm\d*|vram)",
        r"(\d+)\s*gb\b",
    ]:
        m = re.search(pat, t)
        if m:
            gb = int(m.group(1))
            if 2 <= gb <= 128:
                return gb
    return None


def _extract_price(text: str) -> float | None:
    # Take the first dollar amount (handles ranges like "$200.00 to $250.00")
    m = re.search(r"\$([\d,]+\.?\d*)", text)
    if m:
        return float(m.group(1).replace(",", ""))
    return None


def _is_junk(title: str, price: float) -> tuple[bool, str]:
    t = title.lower()
    for kw in JUNK_KEYWORDS:
        if kw in t:
            return True, f"keyword '{kw}'"
    if price < MIN_PRICE:
        return True, f"price ${price:.2f} below minimum"
    if price > MAX_PRICE:
        return True, f"price ${price:.2f} above maximum"
    return False, ""

# =========================================
# CHROME SETUP
# =========================================

def _make_driver() -> webdriver.Chrome:
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    opts.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    driver = webdriver.Chrome(options=opts)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    return driver

# =========================================
# SCRAPING
# =========================================

def _scrape_page(driver: webdriver.Chrome, url: str) -> list[dict]:
    raw = []
    driver.get(url)
    time.sleep(2)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.s-item"))
        )
    except Exception:
        return raw

    items = driver.find_elements(By.CSS_SELECTOR, "li.s-item")

    for item in items:
        try:
            # Title
            title_el = item.find_element(By.CSS_SELECTOR, ".s-item__title")
            title = title_el.text.strip()
            if not title or title.lower() == "shop on ebay":
                continue

            # URL
            try:
                href = item.find_element(By.CSS_SELECTOR, "a.s-item__link").get_attribute("href")
            except NoSuchElementException:
                href = ""

            # Price
            price_el = item.find_element(By.CSS_SELECTOR, ".s-item__price")
            price = _extract_price(price_el.text)
            if price is None:
                continue

            # Shipping cost
            shipping = 0.0
            try:
                ship_el = item.find_element(By.CSS_SELECTOR, ".s-item__shipping, .s-item__freeXDays")
                ship_text = ship_el.text.lower()
                if "free" not in ship_text:
                    sp = _extract_price(ship_el.text)
                    if sp is not None:
                        shipping = sp
            except NoSuchElementException:
                pass

            # Condition
            condition = "Unknown"
            try:
                condition = item.find_element(By.CSS_SELECTOR, ".SECONDARY_INFO").text.strip()
            except NoSuchElementException:
                pass

            raw.append({
                "title":     title,
                "price":     price,
                "shipping":  shipping,
                "condition": condition,
                "url":       href,
            })

        except (StaleElementReferenceException, NoSuchElementException):
            continue
        except Exception:
            continue

    return raw


def scrape_ebay(pages: int = PAGES_PER_QUERY) -> list[dict]:
    # LH_BIN=1  → Buy It Now only (no auction guessing)
    # _sop=15   → sort by Best Match (broad results)
    base = (
        "https://www.ebay.com/sch/i.html"
        "?_nkw={q}&LH_BIN=1&_sop=15&_pgn={p}"
    )
    driver = _make_driver()
    all_raw: list[dict] = []

    try:
        for query in SEARCH_QUERIES:
            encoded = query.replace(" ", "+")
            for page in range(1, pages + 1):
                url = base.format(q=encoded, p=page)
                print(f"  [{query}] page {page} …")
                page_raw = _scrape_page(driver, url)
                all_raw.extend(page_raw)
                time.sleep(1.5)
    finally:
        driver.quit()

    return all_raw

# =========================================
# PROCESSING
# =========================================

def process(raw: list[dict]) -> list[GPUListing]:
    seen: set[str] = set()
    listings: list[GPUListing] = []

    for item in raw:
        url = item.get("url", "")
        # Deduplicate by URL (strip query params for matching)
        url_key = url.split("?")[0]
        if url_key in seen:
            continue
        seen.add(url_key)

        title    = item["title"]
        price    = item["price"]
        shipping = item.get("shipping", 0.0)

        junk, reason = _is_junk(title, price)
        if junk:
            continue

        vram = _extract_vram(title)
        if vram is None or vram < MIN_VRAM_GB:
            continue

        listing = GPUListing(
            title=title,
            price=price,
            shipping=shipping,
            vram_gb=vram,
            condition=item.get("condition", "Unknown"),
            url=url,
        )

        if listing.model_key == "unknown":
            continue

        listings.append(listing)

    return listings

# =========================================
# FIND BEST 4-CARD SET
# =========================================

def find_quad(listings: list[GPUListing]) -> tuple[str, list[GPUListing]]:
    """
    Group by normalized model name, find models with ≥4 listings,
    return the model + its top-4 listings ranked by VRAM/dollar.
    """
    by_model: dict[str, list[GPUListing]] = defaultdict(list)
    for l in listings:
        by_model[l.model_key].append(l)

    candidates = []
    for model, group in by_model.items():
        if len(group) < CARDS_NEEDED:
            continue
        group.sort(key=lambda x: x.vpd, reverse=True)
        top4 = group[:CARDS_NEEDED]
        avg_vpd = sum(g.vpd for g in top4) / CARDS_NEEDED
        candidates.append((model, top4, avg_vpd))

    if not candidates:
        return "", []

    candidates.sort(key=lambda x: x[2], reverse=True)
    best_model, best_4, _ = candidates[0]
    return best_model, best_4

# =========================================
# OUTPUT
# =========================================

def print_results(listings: list[GPUListing], model: str, quad: list[GPUListing]):
    ranked = sorted(listings, key=lambda x: x.vpd, reverse=True)

    print("\n" + "=" * 70)
    print("TOP 20 LISTINGS  —  ranked by VRAM/dollar")
    print("=" * 70)
    for i, l in enumerate(ranked[:20], 1):
        total = l.price + l.shipping
        ship_str = f"+${l.shipping:.0f} ship" if l.shipping else "free ship"
        print(
            f"{i:2}. {l.vram_gb:2}GB | ${total:>7.2f} ({ship_str}) | "
            f"{l.vpd:.4f} GB/$ | {l.title[:50]}"
        )

    print("\n" + "=" * 70)
    print(f"BEST 4-CARD QUAD SET  —  {model.upper()}")
    print("=" * 70)

    if not quad:
        print("Not enough matching listings found. Run with more pages or broader queries.")
        return

    total_cost = sum(l.price + l.shipping for l in quad)
    total_vram = sum(l.vram_gb for l in quad)
    avg_vpd    = sum(l.vpd for l in quad) / CARDS_NEEDED

    print(f"Combined VRAM : {total_vram} GB across {CARDS_NEEDED} cards")
    print(f"Total cost    : ${total_cost:.2f}")
    print(f"Avg VRAM/$    : {avg_vpd:.4f} GB/$\n")

    for i, l in enumerate(quad, 1):
        total = l.price + l.shipping
        print(f"  Card {i}:  {l.title[:65]}")
        print(f"          ${total:.2f} ({l.vram_gb}GB, {l.condition})")
        print(f"          {l.url}")
        print()

    print("=" * 70)
    print("MULTI-GPU BUILD NOTES")
    print("=" * 70)
    print(f"  Motherboard  : needs 4× PCIe x16 slots (x8 electrical is fine for LLM).")
    print(f"                 Good options: ASUS Pro WS X670E-ACE, GIGABYTE TRX50 AERO D.")
    print(f"  LLM inference: CUDA distributes model layers across all GPU VRAM natively.")
    print(f"                 {total_vram}GB combined = can run ~{total_vram // 2}B parameter models in FP16.")
    print(f"  Gaming       : SLI/mGPU is deprecated on RTX 30xx/40xx — only 1 GPU renders.")
    print(f"                 You can assign different GPUs per game/app in the driver.")
    print(f"  Power supply : each {model} draws ~{_tdp_estimate(model)}W → budget ≥{_tdp_estimate(model) * 4 + 200}W PSU.")


def _tdp_estimate(model: str) -> int:
    tdp_map = {
        "rtx 4090": 450, "rtx 4080": 320, "rtx 4070 ti": 285, "rtx 4070": 200,
        "rtx 3090": 350, "rtx 3090 ti": 450, "rtx 3080 ti": 350, "rtx 3080": 320,
        "rtx 3070": 220, "rtx 3060": 170,
        "rx 7900 xtx": 355, "rx 7900 xt": 315, "rx 6900 xt": 300, "rx 6800 xt": 300,
        "a100": 400, "a40": 300, "v100": 300,
    }
    for key, tdp in tdp_map.items():
        if key in model:
            return tdp
    return 250  # conservative default


def save_json(listings: list[GPUListing], model: str, quad: list[GPUListing]):
    out = {
        "all_listings": [
            {
                "title":     l.title,
                "model":     l.model_key,
                "vram_gb":   l.vram_gb,
                "price":     l.price,
                "shipping":  l.shipping,
                "total":     round(l.price + l.shipping, 2),
                "vram_per_dollar": round(l.vpd, 5),
                "condition": l.condition,
                "url":       l.url,
            }
            for l in sorted(listings, key=lambda x: x.vpd, reverse=True)
        ],
        "best_quad": {
            "model":      model,
            "total_vram": sum(l.vram_gb for l in quad),
            "total_cost": round(sum(l.price + l.shipping for l in quad), 2),
            "cards": [
                {"title": l.title, "total": round(l.price + l.shipping, 2), "url": l.url}
                for l in quad
            ],
        },
    }
    path = "gpu_results.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nFull results saved → {path}")

# =========================================
# MAIN
# =========================================

def main():
    print("eBay GPU Quad Finder — 4-card LLM/gaming tower")
    print(f"Searching {len(SEARCH_QUERIES)} queries × {PAGES_PER_QUERY} pages …\n")

    raw = scrape_ebay()
    print(f"\nRaw listings collected : {len(raw)}")

    listings = process(raw)
    print(f"Valid GPU listings     : {len(listings)}")

    if not listings:
        print("\nNo valid listings found. eBay may have changed its layout.")
        return

    model, quad = find_quad(listings)
    print_results(listings, model, quad)
    save_json(listings, model, quad)


if __name__ == "__main__":
    main()
