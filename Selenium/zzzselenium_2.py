from selenium import webdriver

# Create a new Chrome driver
driver = webdriver.Chrome()

# Open a URL
driver.get('https://www.google.com/')

# Put the browser into interactive mode
driver.execute_script("document.body.style.cursor = 'default'")

# Wait for user input
input('Press any key to continue...\n')

# Close the browser
driver.quit()
