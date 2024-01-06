import cv2
# inicialize pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# image stuff
# img = cv2.imread("20231010_130254.jpg")
img = cv2.imread("D:\Documents\github\Free-time-coding\OCR\img.png")

# img = cv2.resize(img, (400, 400))
cv2.imshow("Image", img)
# using pytesseract to get text
text = pytesseract.image_to_string(img)
print(text)





# make sure program doesn't close right away
cv2.waitKey(0)
cv2.destroyAllWindows()
