from ahk import AHK
ahk = AHK(executable_path=r"C:/Program Files/AutoHotkey/AutoHotkey.exe")

# https://www.autohotkey.com/docs/commands/GetKeyState.htm
ahk.type('hello, world!')  # Send keys, as if typed (performs ahk string escapes)
while 1:
    while ahk.key_state('RButton') == 1:
        print('hi')
ahk.sound_beep(frequency=440, duration=1000)
