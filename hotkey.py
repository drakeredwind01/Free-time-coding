import pyautogui

pyautogui.hotkey('control','h')
pyautogui.typewrite('chrome\n',)











'''

https://automatetheboringstuff.com/chapter18/

pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'alt', 'shift', 's')



moveTo(x, y). Moves the mouse cursor to the given x and y coordinates.

moveRel(xOffset, yOffset). Moves the mouse cursor relative to its current position.

dragTo(x, y). Moves the mouse cursor while the left button is held down.

dragRel(xOffset, yOffset). Moves the mouse cursor relative to its current position while the left button is held down.

click(x, y, button). Simulates a click (left button by default).

rightClick(). Simulates a right-button click.

middleClick(). Simulates a middle-button click.

doubleClick(). Simulates a double left-button click.

mouseDown(x, y, button). Simulates pressing down the given button at the position x, y.

mouseUp(x, y, button). Simulates releasing the given button at the position x, y.

scroll(units). Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls down.

typewrite(message). Types the characters in the given message string.

typewrite([key1, key2, key3]). Types the given keyboard key strings.

press(key). Presses the given keyboard key string.

keyDown(key). Simulates pressing down the given keyboard key.

keyUp(key). Simulates releasing the given keyboard key.

hotkey([key1, key2, key3]). Simulates pressing the given keyboard key strings down in order and then releasing them in reverse order.

screenshot(). Returns a screenshot as an Image object. (See Chapter 17 for information on Image objects.)













from system_hotkey.system_hotkey import SystemHotkey

hk = SystemHotkey(use_xlib=False)
hk.unregister(('control', 'a',), callback=lambda e:print('hi'))

while 1:
    pass


Supported modifiers include:

control
shift
super (windows key)
alt



'''





'''
# 2019.12.30.02.16.26.510
from system_hotkey.system_hotkey import SystemHotkey

hk = SystemHotkey(use_xlib=False)
hk.register(('control', 'a',), callback=lambda e:print('hi'))

while 1:
    pass
'''



