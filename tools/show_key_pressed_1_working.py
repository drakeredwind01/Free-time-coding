import keyboard

def print_pressed_keys():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(event.name)

if __name__ == "__main__":
    print_pressed_keys()

'''
doen't work on unknown mouse buttons
maybe a todo for later

'''