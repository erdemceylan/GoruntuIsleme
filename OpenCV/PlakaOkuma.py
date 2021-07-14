import cv2
import pytesseract
import numpy as np
import imutils
import time

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow("Kamera",frame)
    img = cv2.imwrite("test2.jpg",frame)
    img = cv2.imread("test2.jpg")
    img = cv2.resize(img, (720,520))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    filtered = cv2.bilateralFilter(gray,5,250,250)
    edged = cv2.Canny(filtered,30,200)


    contours = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(contours)
    cnts = sorted(cnts,key = cv2.contourArea,reverse = True)[0:10]
    screen = None

    for c in cnts:
        epsilon = 0.018*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)

        if len(approx) == 4:
            screen = approx
            break

    mask = np.zeros(gray.shape,np.uint8)
    new_img = cv2.drawContours(mask,[screen],0,(255,255,255),-1)
    new_img = cv2.bitwise_and(img,img,mask = mask)


    (x,y) = np.where(mask == 255)
    (topx,topy) = (np.min(x),np.min(y))
    (bottomx,bottomy) = (np.max(x),np.max(y))
    cropped = gray[topx:bottomx + 1,topy:bottomy+1]
    print(np.where(mask == 255))


    text = pytesseract.image_to_string(cropped,lang = "tur")
    print("detected text: ",text)
    #cv2.imshow("Foto",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    #cv2.imshow("Car",img)
    time.sleep(2)
cap.release()
cv2.destroyAllWindows()