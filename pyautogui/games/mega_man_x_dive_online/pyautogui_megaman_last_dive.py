import time
import os
'''
never fully realized
the idea was that it was that the most grindy part of the game
was to fully upgrade all the weapons/characters
didn't mind playing the game but the upgrading was tedious
so i was going to automate it 
'''





import webbrowser
import pyautogui

#speak('staring in 3')
#speak('2')
#speak('1')



import pyautogui

def timeout():
  

def find_and_click(image_path_default, message_default, image_path, message):
  """
  This function searches for an image, clicks it if found, and prints a message.
  """
  while True:
    try:
      hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
      if hit:
        print(message)
        pyautogui.click(hit)
        break
      else:
        print(f"Image '{message}' not found, retrying...")
    except pyautogui.ImageNotFoundException:
      pass  # Do nothing on purpose, loop will continue searching

def find_and_click_10(image_path, message):
  """
  This function tries to find an image 10 times with a delay between attempts.
  If not found, it prints a message and moves on.
  """
  for i in range(10):
    if find_and_click(None, None, image_path, message):
      return  # Found the image, exit the function
    time.sleep(1)  # Wait for 1 second before retrying
  print(f"Failed to find '{message}' after 10 tries.")


def find_and_click_or(image_path1, message1, image_path2, message2):
  """
  This function alternates searches for two images until one is found.
  It clicks the found image and prints a message.
  """
  while True:
    if find_and_click(None, None, image_path1, message1):
      return  # Found image1, exit the function
    if find_and_click(None, None, image_path2, message2):
      return  # Found image2, exit the function
    print(f"Neither '{message1}' nor '{message2}' found, retrying...")




  while True:
    any(find_and_click(1),find_and_click(2))
    if find_and_click(None, None, image_path1, message1):
      return  # Found image1, exit the function
    if find_and_click(None, None, image_path2, message2):
      return  # Found image2, exit the function
    print(f"Neither '{message1}' nor '{message2}' found, retrying...")








def main():
  """
  This function calls the find_and_click function for vm and beta images, then presses ctrl+tab.
  """
  find_and_click('/pyautogui/IMAGE_PATH/vm.png', 'hit vm')
  find_and_click('/pyautogui/IMAGE_PATH/beta.png', 'hit beta')
  find_and_click_or('pyautogui/IMAGE_PATH/mega_man_x_dive_online/MXDO_ status_1.png','','pyautogui/IMAGE_PATH/mega_man_x_dive_online/MXDO_ Status_2.png','')
  find_and_click('pyautogui/IMAGE_PATH/mega_man_x_dive_online/MXDO_ level_up.png', 'hit beta')
  pyautogui.hotkey('ctrl', 'tab')  # Press ctrl+tab

if __name__ == "__main__":
  main()

'''
find_and_click_with_retry(image_path, message, max_tries=10, delay=1):
'''





















