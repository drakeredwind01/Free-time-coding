import pythoncom, pyHook
import cv2

def rightdown(event):
    # called when mouse events are received
    while 1:
        print('down')
    # return True to pass the event to other handlers
    return True

def rightup(event):
    # called when mouse events are received
    print('up')
    # return False to pass the event to other handlers
    return False

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.MouseRightDown = rightdown
hm.MouseRightUp = rightup
# set the hook
hm.HookMouse()
# wait forever
pythoncom.PumpMessages()


while 'down' == 1:
    print ('down')
else :
    print ('up')

