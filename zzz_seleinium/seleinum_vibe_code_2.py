
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

# =========================
# CHROME SETUP
# =========================

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

time.sleep(2)

# =========================
# HIGHLIGHT FUNCTION
# =========================

def highlight(el):
    driver.execute_script("""
        arguments[0].style.border='3px solid red';
        arguments[0].style.background='yellow';
    """, el)

# =========================
# SAFE CLICK
# =========================

def safe_click(el):
    try:
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            el
        )

        time.sleep(0.3)

        el.click()

        return True

    except:
        try:
            driver.execute_script(
                "arguments[0].click();",
                el
            )

            return True

        except:
            return False

# =========================
# TEST INPUTS
# =========================

inputs = driver.find_elements(By.TAG_NAME, "input")

print(f"\nFound {len(inputs)} inputs")

for i in range(len(inputs)):

    try:
        inputs = driver.find_elements(By.TAG_NAME, "input")
        el = inputs[i]

        input_type = el.get_attribute("type")

        print(f"\nINPUT {i} | type={input_type}")

        highlight(el)

        # -------------------------
        # TEXT INPUTS
        # -------------------------

        if input_type in [
            "text",
            "password",
            "email",
            "search",
            "url",
            "tel"
        ]:

            el.clear()
            el.send_keys("TEST123")

            print("typed text")

        # -------------------------
        # CHECKBOXES/RADIOS
        # -------------------------

        elif input_type in [
            "checkbox",
            "radio"
        ]:

            safe_click(el)

            print("clicked toggle")

        # -------------------------
        # RANGE SLIDER
        # -------------------------

        elif input_type == "range":

            el.send_keys(Keys.ARROW_RIGHT)
            el.send_keys(Keys.ARROW_RIGHT)

            print("moved slider")

        # -------------------------
        # COLOR PICKER
        # -------------------------

        elif input_type == "color":

            driver.execute_script(
                "arguments[0].value='#00ff00';",
                el
            )

            print("changed color")

        # -------------------------
        # DATE INPUT
        # -------------------------

        elif input_type == "date":

            el.send_keys("2026-06-06")

            print("set date")

        # -------------------------
        # FILE INPUT
        # -------------------------

        elif input_type == "file":

            print("skipped file input")

        # -------------------------
        # SUBMIT BUTTON
        # -------------------------

        elif input_type in [
            "submit",
            "button"
        ]:

            print("skipping submit/button")

        else:

            print("unknown input type")

        time.sleep(0.5)

    except Exception as e:
        print(f"ERROR: {e}")

# =========================
# TEXTAREAS
# =========================

textareas = driver.find_elements(By.TAG_NAME, "textarea")

for i, ta in enumerate(textareas):

    try:
        highlight(ta)

        ta.send_keys("TEST TEXTAREA")

        print(f"textarea {i} typed")

    except Exception as e:
        print(e)

# =========================
# SELECTS
# =========================

selects = driver.find_elements(By.TAG_NAME, "select")

for i, sel in enumerate(selects):

    try:
        highlight(sel)

        options = sel.find_elements(By.TAG_NAME, "option")

        if len(options) > 1:
            options[1].click()

        print(f"select {i} changed")

    except Exception as e:
        print(e)

# =========================
# BUTTONS LAST
# =========================

buttons = driver.find_elements(By.TAG_NAME, "button")

print(f"\nFound {len(buttons)} buttons")

for i, btn in enumerate(buttons):

    try:
        button_type = btn.get_attribute("type")

        text = btn.text.strip()

        print(f"\nBUTTON {i} | {text} | type={button_type}")

        highlight(btn)

        # DON'T CLICK SUBMIT BUTTONS
        if button_type == "submit":

            print("skipping submit")

            continue

        safe_click(btn)

        print("clicked")

        time.sleep(0.5)

    except Exception as e:
        print(e)

print("\nDONE")

input("\nPress ENTER to quit...")

