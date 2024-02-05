from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch a browser
    browser = p.chromium.launch()
    page = browser.new_page()

    # Replace this URL with the target website you want to scrape (not Facebook)
    page.goto("https://www.facebook.com/marketplace")

    # Select the desired image elements
    # Replace this selector with the appropriate one for your target website
    images = page.query_selector_all("img.image-class")

    # Extract image URLs and perform desired actions
    for image in images:
        image_url = image.get_attribute("src")
        print(f"Found image URL: {image_url}")  # You can download or store the image URLs here

    # Close the browser
    browser.close()
