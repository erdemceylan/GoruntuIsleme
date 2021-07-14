import cv2

cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier("gozalgilama.xml")

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray,1.3,8)

    for(x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("Gozler",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()