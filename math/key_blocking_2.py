import keyboard
import time
import threading

blocking_enabled = False
block_thread = None  # Store the thread
'''
untested
'''
def block_y_key():
    global blocking_enabled
    while blocking_enabled:
        if keyboard.is_pressed('y'):
            keyboard.block_key('y')
        time.sleep(0.01)

def toggle_blocking():
    global blocking_enabled, block_thread
    blocking_enabled = not blocking_enabled
    if blocking_enabled:
        print("Y key blocking enabled.")
        block_thread = threading.Thread(target=block_y_key)
        block_thread.daemon = True
        block_thread.start()
    else:
        print("Y key blocking disabled.")
        keyboard.unblock_key('y')
        if block_thread:  # Stop the thread gracefully
            block_thread = None  # Reset the thread variable


def main():
    print("Script started. Press 'b' to toggle Y key blocking. Press 'esc' to exit.")

    while True:
        if keyboard.is_pressed('b'):
            toggle_blocking()
            time.sleep(0.2)  # Debounce

        if keyboard.is_pressed('esc'):
            print("Exiting.")
            if blocking_enabled:  # Ensure unblocking before exiting
                toggle_blocking()
            break

if __name__ == "__main__":
    main()