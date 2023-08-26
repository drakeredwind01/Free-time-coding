
'''

from best logger ever

'''

from pynput.mouse import Listener
import logging

#logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

'''def on_move(x, y):
    #logging.info("Mouse moved to ({0}, {1})".format(x, y))
    print("Mouse moved to ({0}, {1})".format(x, y))'''
print('CoordMode, Mouse, Screen')


def on_click(x, y, button, pressed):
    if pressed:
        #logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        print('Click, {2}, {0}, {1}  '.format(x, y, button))
def on_scroll(x, y, dx, dy):
    #logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

#with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()


'''

MouseClick [, WhichButton, X, Y, ClickCount, Speed, D|U, R]
Click, Left, 0, 50, 300, Rel, 3, 30

ctrl H
Button.

add
CoordMode, Mouse, Screen
f1::
return


'''