import time
import os

#voice stuff
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
#speak('speach online')





import webbrowser
import pyautogui

#speak('staring in 3')
#speak('2')
#speak('1')




def imNotARobot():
    speak('how dare you question me')
    imNotARobot = pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\im not a robot.png', confidence=0.8)
    pyautogui.click(pyautogui.center(imNotARobot))
    print(imNotARobot)
def coinFarm():
    speak('opening coin-farm')
    webbrowser.open('https://coin-farm.net/account/store')
    time.sleep(3)
    COLLECTALL = pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\coin-farm COLLECT ALL.png', confidence=0.8)
    pyautogui.click(pyautogui.center(COLLECTALL))
    #print(pyautogui.locateOnScreen("start.png"))
    print(COLLECTALL)
def moonbit():
    speak('opening coin-farm')
    webbrowser.open('https://moonbit.co.in/')
    time.sleep(3)
    pyautogui.scroll(-20)
    def moonbitclaimnow():
        moonbitclaimnow = False
        while moonbitclaimnow==False:
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitclaimnow.png') is not None):
                moonbitclaimnow = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitclaimnow.png', confidence=0.6)
                print(hit)
                pyautogui.click(hit)
                pyautogui.scroll(-100)
    def moonbitimnotarobot():
        moonbitimnotarobot = False
        while moonbitimnotarobot==False:
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitimnotarobot.png') is not None):
                moonbitimnotarobot = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitimnotarobot.png', confidence=0.6)
                print(hit)
                pyautogui.click(hit)
    def moonbitsubmit():
        moonbitsubmit = False
        while moonbitsubmit==False:
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitsubmit.png') is not None):
                moonbitsubmit = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\moonbitsubmit.png', confidence=0.6)
                print(hit)
                pyautogui.click(hit)
    moonbitclaimnow()
    moonbitimnotarobot()
    moonbitsubmit()
def bitfun():
    def bitfunclaimnow():
        bitfunclaimnow = False
        while bitfunclaimnow==False:
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\bitfunclaimnow.png', confidence=0.8) is not None):
                bitfunclaimnow = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\bitfunclaimnow.png', confidence=0.8)
                print(hit)
                pyautogui.click(hit)
                time.sleep(3)
                pyautogui.moveRel(xOffset=100,yOffset=100,duration=3,pause=3)
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\bitfunclaimnow.png', confidence=0.8) is not None):
                bitfunclaimnow = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\bitfunclaimnow.png', confidence=0.8)
                print(hit)
                time.sleep(3)
    def imnotarobot():
        imnotarobot = False
        while imnotarobot==False:
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\imnotarobot.png') is not None):
                imnotarobot = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\imnotarobot.png', confidence=0.8)
                print(hit)
                pyautogui.click(hit)
                time.sleep(1)
    def claim():
        claim = False
        while claim==False:
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\claim.png') is not None):
                claim = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\claim.png', confidence=0.8)
                print(hit)
                pyautogui.click(hit)
                time.sleep(1)
    def close():
        close = False
        while close==False:
            if (pyautogui.locateOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\close.png') is not None):
                close = True
                hit = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\close.png', confidence=0.8)
                print(hit)
                pyautogui.click(hit)
                time.sleep(1)
    speak('opening bitfun')
    webbrowser.open('https://bitfun.co/games')
    time.sleep(5)
    bitfunclaimnow()
    imnotarobot()
    claim()
    close()
def kimcartoon():
    def vm():
        while True:
            try:
                hit = pyautogui.locateCenterOnScreen(
                    'D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\vm.png', confidence=0.8)
                print('hit vm')
                pyautogui.click(hit)
                break
            except pyautogui.ImageNotFoundException:
                print('Image not found, retrying...')
                pass
    def beta():
        while True:
            try:
                hit = pyautogui.locateCenterOnScreen(
                    'D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\beta.png', confidence=0.8)
                print('hit beta')
                pyautogui.click(hit)
                break
            except pyautogui.ImageNotFoundException:
                print('Image not found, retrying...')
                pass
    def download_this_video():
        while True:
            try:
                hit = pyautogui.locateCenterOnScreen(
                    'D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\download_this_video.png',
                    confidence=0.8)
                print('hit download_this_video')
                pyautogui.click(hit)
                break
            except pyautogui.ImageNotFoundException:
                print('Image not found, retrying...')
                pass
    def start_download():
        while True:
            try:
                hit = pyautogui.locateCenterOnScreen(
                    'D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\start_download.png',
                    confidence=0.8)
                print('hit start_download')
                pyautogui.click(hit)
                break
            except pyautogui.ImageNotFoundException:
                print('Image not found, retrying...')
                pass

    def down_continue_background():
        while True:
            try:
                hit = pyautogui.locateCenterOnScreen(
                    'D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\down_continue_background.png',
                    confidence=0.8)
                print('hit down_continue_background')
                pyautogui.click(hit)
                break
            except pyautogui.ImageNotFoundException:
                print('Image not found, retrying...')
                pass
    vm()
    beta()
    download_this_video()
    start_download()
    down_continue_background()
if __name__ == '__main__':
    #start()
    kimcartoon()
    #coinFarm()
    #moonbit()
    #moonbit2()
    #bitfun()


































