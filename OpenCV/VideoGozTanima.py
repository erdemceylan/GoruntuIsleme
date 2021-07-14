import cv2

cap = cv2.VideoCapture("eye.mp4")
eye_cascade = cv2.CascadeClassifier("gozalgilama.xml")

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray,1.3,2)

    for(x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Gozler",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


