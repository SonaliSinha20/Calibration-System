import numpy as np
import cv2
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
REC_X1=250
REC_Y1=100
REC_X2=450
REC_Y2=400
REC_RED=0
REC_GREEN=255
REC_BLUE=0
REC_WID=5
TEXT_RED=0
TEXT_GREEN=255
TEXT_BLUE=0
TEXT_X=10
TEXT_Y=30
TEXT_SIZE=0.7
TEXT_WIDTH=2
REC_FACE_BLUE=255
REC_FACE_GREEN=0
REC_FACE_RED=0
REC_FACE_WIDTH=2
REC_CENTER_X=350
REC_CENTER_Y=250


while(True):

    
    ret, img = cap.read()
 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    cv2.rectangle(img, (REC_X1, REC_Y1), (REC_X2, REC_Y2), (REC_BLUE, REC_GREEN, REC_RED), REC_WID)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(REC_FACE_RED,REC_FACE_GREEN,REC_FACE_BLUE),REC_FACE_WIDTH)
        CENTER_X=(x+(w/2))
        CENTER_Y=(y+(h/2))


        if abs(CENTER_X - REC_CENTER_X)>=abs(CENTER_Y - REC_CENTER_Y):     
            if CENTER_X<REC_CENTER_X and x<REC_X1:
                cv2.putText(img, "move left", (TEXT_X,TEXT_Y), cv2.FONT_HERSHEY_SIMPLEX, TEXT_SIZE, (TEXT_BLUE, TEXT_GREEN, TEXT_RED), TEXT_WIDTH)
            elif CENTER_X>REC_CENTER_X and x+w>REC_X2:
                cv2.putText(img, "move right", (TEXT_X,TEXT_Y), cv2.FONT_HERSHEY_SIMPLEX,TEXT_SIZE, (TEXT_BLUE, TEXT_GREEN, TEXT_RED), TEXT_WIDTH)
        else:        
            if CENTER_Y<REC_CENTER_Y and y<REC_Y1:
                cv2.putText(img, "move down", (TEXT_X,TEXT_Y), cv2.FONT_HERSHEY_SIMPLEX, TEXT_SIZE, (TEXT_BLUE, TEXT_GREEN, TEXT_RED), TEXT_WIDTH)
            elif CENTER_Y>REC_CENTER_Y and y+h>REC_Y2:
                cv2.putText(img, "move up", (TEXT_X,TEXT_Y), cv2.FONT_HERSHEY_SIMPLEX, TEXT_SIZE, (TEXT_BLUE, TEXT_GREEN, TEXT_RED), TEXT_WIDTH)
        
        area = (min(REC_X2,x+w)-max(REC_X1,x))*((min(REC_Y2,y+h)-max(REC_Y1,y)))
        A = w*h
        per = 100*area/A
        cv2.putText(img, str(per), (TEXT_X,TEXT_Y+30), cv2.FONT_HERSHEY_SIMPLEX, TEXT_SIZE, (TEXT_BLUE, TEXT_GREEN, TEXT_RED), TEXT_WIDTH)     
 
    cv2.imshow('face', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

