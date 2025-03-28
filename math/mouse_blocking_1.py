import time
import keyboard
import pyautogui


def toggle_mouse_blocking():
    test = pyautogui.getInfo() #what does this do?
    print(test)
    pyautogui.moveTo(500,500)
    time.sleep(3)

def main():
    print("Script started. Press 'm' to toggle mouse blocking. Press 'esc' to exit.")

    while True:
        if keyboard.is_pressed('m'):
            toggle_mouse_blocking()
            time.sleep(0.2)  # Debounce

        if keyboard.is_pressed('esc'):
            print("Exiting.")
            if blocking_mouse:
                toggle_mouse_blocking()
            break

if __name__ == "__main__":
    main()
