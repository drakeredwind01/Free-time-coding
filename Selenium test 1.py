from selenium import webdriver
import pyautogui
import time

from selenium.webdriver.chrome import service



folder_path = r'C:\Windows\SoftwareDistribution\Download'
driver = webdriver.Chrome('C:\\Users\\drivers\\chromedriver_114_0_5735_90.exe')

driver.get('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div').click()

#get the captcha buster
addextension = False
while addextension==False:
    if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\addextension.png') is not None):
        addextension = True
        hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\addextension.png', confidence=0.8)
        print(hit)
        pyautogui.click(hit)


driver.get("http://moonbit.co.in/faucet#");
#driver.maximize_window()
if (driver.find_element_by_id('BodyPlaceholder_PaymentAddressTextbox')):
    PaymentAddressTextbox = driver.find_element_by_id('BodyPlaceholder_PaymentAddressTextbox')
    PaymentAddressTextbox.send_keys('3357Xyu566scman68Kky2SKECaGKGz12fN')
    SignInButton = driver.find_element_by_id('SignInButton')
    SignInButton.click()
    time.sleep(3)
    moonbitimnotarobot = False
    while moonbitimnotarobot == False:
        if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitimnotarobot.png') is not None):
            moonbitimnotarobot = True
            hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitimnotarobot.png', confidence=0.6)
            print(hit)
            pyautogui.click(hit)
    time.sleep(3)
    solverbutton = False
    while solverbutton==False:
        if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\solverbutton.png') is not None):
            solverbutton = True
            hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\solverbutton.png', confidence=0.8)
            print(hit)
            pyautogui.click(hit)





SubmitButton = driver.find_elements_by_id('SubmitButton')
SubmitButton.clear()


driver.quit()
