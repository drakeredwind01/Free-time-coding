import cv2
img = cv2.imread("D:/documents/GitHub/Free time coding/OCR/image.png")
img = cv2.resize(img, (400, 400))
cv2.imshow("Image", img)

import pytesseract
# pytesseract.pytesseract.tesseract_cmd=r'C:Program FilesTesseract-OCRtesseract.exe'
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(img)
print(text)






cv2.waitKey(0)
cv2.destroyAllWindows()
