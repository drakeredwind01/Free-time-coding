from pynput import mouse


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('yes')

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
