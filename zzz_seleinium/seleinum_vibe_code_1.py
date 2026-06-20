from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.options import Options
import time

# =========================
# CHROME SETUP
# =========================

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

# =========================
# TARGET WEBSITE
# =========================

# driver.get("https://example.com")
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get("https://www.google.com")

time.sleep(3)

actions = ActionChains(driver)

# =========================
# HELPER FUNCTIONS
# =========================

def highlight(element):
    driver.execute_script(
        """
        arguments[0].style.border='3px solid red';
        arguments[0].style.background='yellow';
        """,
        element,
    )


def safe_click(element):
    try:
        element.click()
        return True
    except:
        try:
            driver.execute_script("arguments[0].click();", element)
            return True
        except:
            return False


def test_input(element):
    try:
        element.clear()
    except:
        pass

    try:
        element.send_keys("TEST_INPUT")
        return True
    except:
        return False


# =========================
# BUTTONS
# =========================

buttons = driver.find_elements(By.TAG_NAME, "button")

print(f"\nFound {len(buttons)} buttons")

for i, button in enumerate(buttons):
    try:
        highlight(button)

        text = button.text.strip()

        result = safe_click(button)

        print(f"[BUTTON {i}] '{text}' -> {result}")

        time.sleep(0.5)

    except Exception as e:
        print(f"[BUTTON {i}] ERROR -> {e}")


# =========================
# LINKS
# =========================

links = driver.find_elements(By.TAG_NAME, "a")

print(f"\nFound {len(links)} links")

for i, link in enumerate(links):
    try:
        href = link.get_attribute("href")

        if href:
            print(f"[LINK {i}] {href}")

    except Exception as e:
        print(f"[LINK {i}] ERROR -> {e}")


# =========================
# INPUT FIELDS
# =========================

inputs = driver.find_elements(By.TAG_NAME, "input")

print(f"\nFound {len(inputs)} inputs")

for i, inp in enumerate(inputs):
    try:
        input_type = inp.get_attribute("type")

        highlight(inp)

        print(f"[INPUT {i}] type={input_type}")

        # TEXT INPUTS
        if input_type in ["text", "email", "password", "search", None]:
            result = test_input(inp)
            print(f"  typed -> {result}")

        # CHECKBOXES / RADIOS
        elif input_type in ["checkbox", "radio"]:
            result = safe_click(inp)
            print(f"  toggled -> {result}")

        # RANGE SLIDERS
        elif input_type == "range":
            inp.send_keys(Keys.ARROW_RIGHT)
            print("  slider moved")

        time.sleep(0.5)

    except Exception as e:
        print(f"[INPUT {i}] ERROR -> {e}")


# =========================
# TEXTAREAS
# =========================

textareas = driver.find_elements(By.TAG_NAME, "textarea")

print(f"\nFound {len(textareas)} textareas")

for i, ta in enumerate(textareas):
    try:
        highlight(ta)

        ta.send_keys("TEST_TEXTAREA")

        print(f"[TEXTAREA {i}] typed")

    except Exception as e:
        print(f"[TEXTAREA {i}] ERROR -> {e}")


# =========================
# SELECT DROPDOWNS
# =========================

selects = driver.find_elements(By.TAG_NAME, "select")

print(f"\nFound {len(selects)} selects")

for i, sel in enumerate(selects):
    try:
        highlight(sel)

        options = sel.find_elements(By.TAG_NAME, "option")

        if len(options) > 1:
            options[1].click()

        print(f"[SELECT {i}] changed")

    except Exception as e:
        print(f"[SELECT {i}] ERROR -> {e}")


# =========================
# CONTENTEDITABLE
# =========================

editable = driver.find_elements(By.CSS_SELECTOR, "[contenteditable='true']")

print(f"\nFound {len(editable)} editable elements")

for i, el in enumerate(editable):
    try:
        highlight(el)

        el.send_keys("TEST_EDITABLE")

        print(f"[EDITABLE {i}] typed")

    except Exception as e:
        print(f"[EDITABLE {i}] ERROR -> {e}")


# =========================
# SUMMARY
# =========================

print("\nDONE TESTING")

input("\nPress ENTER to quit...")

