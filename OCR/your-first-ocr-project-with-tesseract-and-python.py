import cv2
# inicialize pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# image stuff
# img = cv2.imread("D:/documents/GitHub/Free time coding/OCR/image.png")
img = cv2.imread("/OCR/Title_level_assistant_associate_staff_senior_principal_chief.jpg")
img = cv2.resize(img, (400, 400))
cv2.imshow("Image", img)
# using pytesseract to get text
text = pytesseract.image_to_string(img)
print(text)





# make sure program doesn't close right away
cv2.waitKey(0)
cv2.destroyAllWindows()
