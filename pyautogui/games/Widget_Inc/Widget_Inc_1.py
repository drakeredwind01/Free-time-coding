import pyautogui
import time
'''
these scripts help to upgrade the buildings by 
finding the caution sign
the screen has to be zoomed in at the right zoom level for
the caution sign to match the image it's looking for
'''


def find_and_click(count, image_path, message):
  """
  This function searches for an image, clicks it if found, and prints a message.
  """
  while True:
    try:
      hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
      # hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(1465, 508, 1608, 622))

      if hit:
        # print(message)
        count + 1
        print(f"{count} {message}")
        pyautogui.click(hit)
        break
      else:
        print(f"Image '{message}' not found, retrying...")
    except pyautogui.ImageNotFoundException:
      pass  # Do nothing on purpose, loop will continue searching


def main():
  # time.sleep(5)
  # pyautogui.keyDown('ctrl')  # hold down the ctrl key
  i = 0
  while True:
    try:
      find_and_click(i,'Widget_Inc_to_upgrade_1.png', 'hit Widget_Inc_to_upgrade_1')
    except:
      pass  # Do nothing on purpose, loop will continue searching




if __name__ == "__main__":
  main()


'''
  pyautogui.hotkey('ctrl', 'tab')  # Press ctrl+tab
  pyautogui.keyDown('ctrl')  # hold down the ctrl key
  
'''