import pyautogui
import time


'''
don't redo 
    upgrades
    monkeys

remember you need:
    snip
    gimp


'''
def ninja():
    ninja = False
    while ninja==False:
        if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\ninja.png') is not None):
            ninja = True
            buy = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\ninja.png', confidence=0.8)
            print(buy)
            pyautogui.click(buy)

def ninjaup01():
    ninjaup01 = False
    while ninjaup01==False:
        if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\ninjaup01.png') is not None):
            ninjaup01 = True
            buyninjaup01 = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\ninjaup01.png', confidence=0.8)
            print(buyninjaup01)
            pyautogui.click(buyninjaup01)



def ninjaup10():
    ninjaup10 = False
    while ninjaup10==False:
        if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\ninjaup10.png') is not None):
            ninjaup10 = True
            buyninjaup10 = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\ninjaup10.png', confidence=0.8)
            print(buyninjaup10)
            pyautogui.click(buyninjaup10)


def bomb():
    bomb = False
    while bomb==False:
        if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\bomb.png') is not None):
            bomb = True
            buy = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\bomb.png', confidence=0.8)
            print(buy)
            pyautogui.click(buy)










def go():
    go = False
    while go==False:
        if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\go.png') is not None):
            go = True
            pressgo = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\go.png', confidence=0.8)
            print(pressgo)
            pyautogui.click(pressgo)

def faster():
    faster = False
    while faster==False:
        if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\faster.png') is not None):
            faster = True
            buy = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\faster.png', confidence=0.8)
            print(buy)
            pyautogui.click(buy)


def nonstop():
    nonstop = False
    while nonstop==False:
        if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\nonstop.png') is not None):
            nonstop = True
            buy = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\nonstop.png', confidence=0.8)
            print(buy)
            pyautogui.click(buy)





def highdesert():
    go()
    faster()
    nonstop()
    ninja()
    pyautogui.click(376, 625)
    ninjaup01()
    ninjaup10()
    time.sleep(3)
    bomb()
    pyautogui.click(290, 720)
    ninja()
    pyautogui.click(416, 625)
    ninjaup01()
    ninjaup10()
    pyautogui.click(376, 625)



stagefound = False
while stagefound==False:
    # highdesert
    if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\high desert.PNG') is not None):
        stagefound = True
        highdesert()














'''
D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\

if (pyautogui.locateOnScreen('zzzselenium.py.PNG') is not None):
    pyautogui.hotkey('win', 'l')
    
    claimnow = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\bitfun claim now.png', confidence=0.8)
    pyautogui.click(claimnow)

'''









