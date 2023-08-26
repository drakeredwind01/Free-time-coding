import pyautogui
import time

skipads = False
while skipads==False:
    print('')
    time.sleep(1)
    if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\youtube\\skipads.png', confidence=0.8) is not None):
        skipads = True
        hit = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\youtube\\skipads.png', confidence=0.8)
        print(hit)
        pyautogui.click(hit)
    if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\youtube\\skipads.png',confidence=0.8) is not None):
        skipads = True
        hit = pyautogui.locateCenterOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\youtube\\skipads.png', confidence=0.8)
        print(hit)
        pyautogui.click(hit)


'''


Mouse clicked at (1077, 686) with Button.right
Mouse clicked at (1217, 686) with Button.right
Mouse clicked at (1077, 736) with Button.right
Mouse clicked at (1217, 734) with Button.right



'''







