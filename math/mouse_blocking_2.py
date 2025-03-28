import time
import keyboard
import pyautogui

blocking_mouse = False
script_active = True

def toggle_mouse_blocking():
    global blocking_mouse, script_active  # Make script_active global as well
    blocking_mouse = not blocking_mouse

    if blocking_mouse:
        print("Mouse movement blocked.")
        while blocking_mouse and script_active:
            pyautogui.moveTo(500, 500)
            time.sleep(.5)
            if not script_active:
                blocking_mouse = False
                print("Mouse movement unblocked.")
                break
            if keyboard.is_pressed('esc'):
                blocking_mouse = False
                script_active = False
                print("Exiting.")
                exit()
    else:
        print("Mouse movement unblocked.")



def main():
    global script_active
    print("Script started. Press 'm' to toggle mouse blocking. Press 'esc' to exit.")

    while script_active:
        if keyboard.is_pressed('m'):
            toggle_mouse_blocking()
            while keyboard.is_pressed('m'):  # Debouncing
                time.sleep(1)
        if keyboard.is_pressed('esc'):
            script_active = False
            print("Exiting.")
            break

if __name__ == "__main__":
    main()