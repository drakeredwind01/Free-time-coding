import pytesseract
import cv2 # For loading image

img = cv2.imread('D:/documents/GitHub/Free time coding/OCR/image.png')
text = pytesseract.image_to_string(img, config='-l eng --oem 1 --psm 6')
print(text)