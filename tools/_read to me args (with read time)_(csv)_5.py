import time
import win32clipboard
import pyautogui
import keyboard  # Use keyboard library for key detection

# Voice stuff (optional)
import pyttsx3

'''
activate tf
python "D:\Documents\github\Free-time-coding\tools\_read to me args (with read time)_(csv)_5.py" "
'''



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)
engine.setProperty('rate', 350)
engine.setProperty('pitch', 1)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def read_clipboard_and_process():
    """Reads clipboard content, calculates reading time, and prints results."""
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        starttime = time.time()
        print(data)
        argCharicters = len(data)
        # print(argCharicters) redundant
        print(f"__________________________________________________")  # testing
        print(f"Number of charicters: {argCharicters}")  # testing

        def check_space(argv):
            return argv.count(" ")

        word_count = {check_space(data) + 1}
        print(f"Number of words: {check_space(data) + 1}")


        speak(data)
        curtime = (time.time() - starttime)
        print(f"AI TIME: {curtime}")  # testing
        print(f"AI W/M: {int(argCharicters / (curtime / 60))}")  # testing
        print(f"Human TIME: {int(word_count.pop() / 2.5)}")  # Get and remove the only element, then divide
        print(f"Human W/M: 150")  # testing

        total_time_saved = int(curtime - ((check_space(data) + 1) / 150))  # wrong

        print(
            f"Total Time Saved: {total_time_saved} seconds"
        )  # testing

        # for google sheets
        print(
            f"{argCharicters},{word_count},{curtime},{total_time_saved}"
        )
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    except (AttributeError, win32clipboard.error):
        print("Error: Clipboard access denied or pyautogui/win32clipboard not installed.")

def print_simple():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    speak(data)


if __name__ == "__main__":
    # keyboard.add_hotkey("q", read_clipboard_and_process)
    keyboard.add_hotkey("q", print_simple)
    keyboard.wait()
