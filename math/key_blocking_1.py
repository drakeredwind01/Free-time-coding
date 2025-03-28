import keyboard
import time
import threading

blocking_enabled = False
'''
b does not work to reenable y presses

'''
def block_y_key():
    global blocking_enabled
    while blocking_enabled:
        if keyboard.is_pressed('y'):  # Check if 'y' is pressed
            # Consume the 'y' key event (prevent it from being processed)
            keyboard.block_key('y')
        time.sleep(0.01)  # Small delay to avoid excessive CPU usage

def toggle_blocking():
    global blocking_enabled
    blocking_enabled = not blocking_enabled  # Toggle the flag
    if blocking_enabled:
        print("Y key blocking enabled.")
        block_thread = threading.Thread(target=block_y_key)  # Start blocking in a separate thread
        block_thread.daemon = True  # Allow the main thread to exit even if the blocking thread is running
        block_thread.start()

    else:
        print("Y key blocking disabled.")
        keyboard.unblock_key('y')  # Unblock the 'y' key



def main():
    print("Script started. Press 'b' to toggle Y key blocking. Press 'esc' to exit.")

    while True:
        if keyboard.is_pressed('b'):  # Toggle blocking with 'b'
            toggle_blocking()
            time.sleep(0.2)  # Debounce

        if keyboard.is_pressed('esc'):
            print("Exiting.")
            if blocking_enabled:  # Ensure unblocking before exiting
                toggle_blocking() # disable y key blocking
            break

if __name__ == "__main__":
    main()