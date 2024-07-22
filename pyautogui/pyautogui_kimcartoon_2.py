import pyautogui


# image_path = "D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\vm.png"  # Store path in a variable

# Load the image once (optional for potential efficiency improvement)
# image = pyautogui.screenshot(image_path)  # Uncomment if needed

def cookieclicker1():
    while True:
        try:
            hit = pyautogui.locateCenterOnScreen('D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\vm.png', confidence=0.8)
            print('hit cookieclicker1')
            pyautogui.click(hit)
            break  # Exit the loop once the image is found
        except pyautogui.ImageNotFoundException:
            print('Image not found, retrying...')
            pass  # Do nothing on purpose, loop will continue searching

if __name__ == "__main__":
    cookieclicker1()





f2::
  SEND,^c
  SEND,def ^v():{ENTER}
  SEND,while True:{ENTER}
  SEND,try:{ENTER}
  SEND,hit = pyautogui.locateCenterOnScreen('D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\^v.png', confidence=0.8){ENTER}
  SEND,print('hit ^v'){ENTER}
  SEND,pyautogui.click(hit){ENTER}
  SEND,break{ENTER}
  SEND,except pyautogui.ImageNotFoundException:{ENTER}
  SEND,print('Image not found, retrying...'){ENTER}
  SEND,pass{ENTER}
  return




