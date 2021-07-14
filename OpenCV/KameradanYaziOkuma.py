import cv2
import pytesseract
import numpy as np
import imutils
import time
from PIL import Image

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow("Kamera",frame)
    img = cv2.imwrite("test2.jpg",frame)
    img = cv2.imread("test2.jpg")
    img = cv2.resize(img, (720,520))
    img = Image.open("test2.jpg")
    text = pytesseract.image_to_string(img, lang = "tur")
    print(text)
    #cv2.imshow("Foto",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    #cv2.imshow("Car",img)
    time.sleep(2)
cap.release()
cv2.destroyAllWindows()