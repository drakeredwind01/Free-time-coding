import time
import os

#voice stuff
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
#speak('speach online')





import webbrowser
import pyautogui

#speak('staring in 3')
#speak('2')
#speak('1')



import pyautogui
import pyautogui

def find_and_click(image_path, message):
  """
  This function searches for an image, clicks it if found, and prints a message.
  """
  while True:
    try:
      print(f"searching '{image_path}'")
      hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
      if hit:
        print(message)
        pyautogui.click(hit)
        break
      else:
        print(f"Image '{message}' not found, retrying...")
    except pyautogui.ImageNotFoundException:
      pass  # Do nothing on purpose, loop will continue searching

def find_2_and_click(image_path_1, message_1, image_path_2, message_2):
  """
  This function searches for an image, clicks it if found, and prints a message.
  """
  while True:
    try:
      print(f"searching '{image_path_1}'")
      hit = pyautogui.locateCenterOnScreen(image_path_1, confidence=0.8)
      if hit:
        print(message_1)
        pyautogui.click(hit)
        pass
      print(f"searching '{image_path_2}'")
      hit_2 = pyautogui.locateCenterOnScreen(image_path_2, confidence=0.5)
      if hit_2:
        print(message_2)
        pyautogui.click(hit_2)
      # pass  # Do nothing on purpose, loop will continue searching
    except pyautogui.ImageNotFoundException:
      print(f"Image not found, retrying...")
      # Optionally, add a delay between retries
      # time.sleep(1)  # Uncomment to introduce a delay
      pass

def main():
  """
  This function calls the find_and_click function for vm and beta images, then presses ctrl+tab.
  This loop will repeat the entire process indefinitely.
  """
  while True:
    mousepose = pyautogui.position()
    find_and_click('IMAGE_PATH/wco_tv_play_button.png', 'hit wco_tv_play_button.png')
    pyautogui.moveRel(xOffset=-50,yOffset=0)
    pyautogui.click()
    find_and_click('D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\download_this_video.png', 'hit download_this_video')
    # find_2_and_click('D:/Documents/github/Free-time-coding/pyautogui/IMAGE_PATH/start_download.png', 'hit start_download', 'D:/Documents/github/Free-time-coding/pyautogui/IMAGE_PATH/start_download_2.png', 'hit start_download_2')
    find_and_click('D:/Documents/github/Free-time-coding/pyautogui/IMAGE_PATH/start_download_2.png', 'hit start_download_2')
    find_and_click('D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\down_continue_background.png', 'hit down_continue_background')
    pyautogui.hotkey('ctrl', 'tab')  # Press ctrl+tab
    pyautogui.moveTo(mousepose)
    time.sleep(1)
    pyautogui.scroll(-700) # Press page down

if __name__ == "__main__":
  main()




