from selenium import webdriver
from bs4 import BeautifulSoup

# Create a new Selenium webdriver
chrome_driver_path = r'D:\documents\GitHub\Free time coding\_apps\chromedriver_118_0_5993_70.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Go to the OfferUp website
driver.get("https://offerup.com/")

# Search for "boat stuff"
search_bar = driver.find_element_by_name("search")
search_bar.send_keys("boat stuff")
search_bar.submit()

# Filter the results to only show items under $1000
price_filter = driver.find_element_by_xpath("//a[@data-value='under1000']")
price_filter.click()

# Wait for the page to load
driver.implicitly_wait(10)

# Get the HTML of the page
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all of the boat stuff items
boat_stuff_items = soup.find_all("div", class_="listing-card")

# Create a list to store the boat stuff items
boat_stuff_list = []

# Iterate over the boat stuff items and extract the information
for boat_stuff_item in boat_stuff_items:
    title = boat_stuff_item.find("h2").text
    price = boat_stuff_item.find("span", class_="price").text
    description = boat_stuff_item.find("p", class_="description").text

    # Add the boat stuff item to the list
    boat_stuff_list.append({
        "title": title,
        "price": price,
        "description": description
    })

# Print the boat stuff list
print(boat_stuff_list)

# Close the Selenium webdriver
driver.quit()
