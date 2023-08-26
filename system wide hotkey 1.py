#pyhk.addHotkey(SomeHotkey,SomeFunction)



'''
https://stackoverflow.com/questions/3337973/set-global-hotkey-with-python-2-6

The RegisterHotKey method of the wx.Window class is what you're looking for -- as the docs say,

Registers a system wide hotkey. Every time the user presses the hotkey registered here, this window will receive a hotkey event. It will receive the event even if the application is in the background and does not have the input focus because the user is working with some other application. To bind an event handler function to this hotkey use EVT_HOTKEY with an id equal to hotkeyId. Returns True if the hotkey was registered successfully.

So, make an instance of `wx.Window, register the hotkey you want with this method, and possibly do a PushEventHandler if ypu'd rather handle the event(s) in a separate event handler rather than in the window itself (the latter being the default).

Is there anything else in this procedure that is not entirely clear to you...? If so, please edit your question to add whatever further problems you may have!


http://timgolden.me.uk/python/win32_how_do_i/catch_system_wide_hotkeys.html


'''





#
# After a post to c.l.py by Richie Hindle:
# http://groups.google.com/groups?th=80e876b88fabf6c9
#
import os
import sys
import ctypes
from ctypes import wintypes
import win32con

byref = ctypes.byref
user32 = ctypes.windll.user32

HOTKEYS = {
  1 : (win32con.VK_F3, win32con.MOD_WIN),
  2 : (win32con.VK_F4, win32con.MOD_WIN)
}

def handle_win_f3 ():
  os.startfile (os.environ['TEMP'])

def handle_win_f4 ():
  user32.PostQuitMessage (0)

HOTKEY_ACTIONS = {
  1 : handle_win_f3,
  2 : handle_win_f4
}

#
# RegisterHotKey takes:
#  Window handle for WM_HOTKEY messages (None = this thread)
#  arbitrary id unique within the thread
#  modifiers (MOD_SHIFT, MOD_ALT, MOD_CONTROL, MOD_WIN)
#  VK code (either ord ('x') or one of win32con.VK_*)
#
for id, (vk, modifiers) in HOTKEYS.items ():
  print ("Registering id", id, "for key", vk)
  if not user32.RegisterHotKey (None, id, modifiers, vk):
    print ("Unable to register id", id)

#
# Home-grown Windows message loop: does
#  just enough to handle the WM_HOTKEY
#  messages and pass everything else along.
#
try:
  msg = wintypes.MSG ()
  while user32.GetMessageA (byref (msg), None, 0, 0) != 0:
    if msg.message == win32con.WM_HOTKEY:
      action_to_take = HOTKEY_ACTIONS.get (msg.wParam)
      if action_to_take:
        action_to_take ()

    user32.TranslateMessage (byref (msg))
    user32.DispatchMessageA (byref (msg))

finally:
  for id in HOTKEYS.keys ():
    user32.UnregisterHotKey (None, id)









