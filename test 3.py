
from pynput.mouse import Listener








if __name__ == '__main__':
    def on_click(x, y, button, pressed):
        if pressed:
            print("mouse pressed at ", x, y, button)
    with Listener(on_click=on_click) as Listener:
        Listener.join()
