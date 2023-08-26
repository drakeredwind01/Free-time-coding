import time

from selenium import webdriver
from selenium.webdriver.chrome import service


webdriver_service = service.Service('D://documents//ai//python\my-first-conda-project\divers\operadriver_win64\operadriver.exe')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get('https://www.linkedin.com/')
#input_txt = driver.find_element_by_name('homepage-basic_google-sign-in-button')
time.sleep(2)
#homepage_basic_google_sign_in_button = driver.find_element_by_name("google-sign-in-cta__text")
homepage_basic_google_sign_in_button = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[1]/form/button")
homepage_basic_google_sign_in_button.click()
time.sleep(5)



handles = driver.window_handles
size = len(handles)

for x in range(size):
  driver.switch_to.window(handles[x])
  print(driver.title)



'''
handle = driver.getWindowHandles();
print()
print('1 win name is ' + handle)
firstWinHandle = driver.getWindowHandle(); handle.remove(firstWinHandle);
winHandle=handle.iterator().next();
if (winHandle!=firstWinHandle):
    secondWinHandle = handle #Storing handle of second window handle
driver.switchTo().window(secondWinHandle);
'''


googleAccountIdentifier = driver.find_element_by_name('identifier')
googleAccountIdentifier.send_keys('drakeredwind01@gmail.com\n')

#input_txt.send_keys('operadriver\n')

#time.sleep(5) #see the result
#driver.quit()