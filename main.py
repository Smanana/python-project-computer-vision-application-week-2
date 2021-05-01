#import libraries

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses')

#video cam variable
cam = cv2.VideoCapture(0)

#
while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    #Detects the face
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = {y:y+h, x:x+w}
        roi_color = {y:y+h, x:x+w}

        #eyes variable
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew.eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 0)

    #within the whileloop,outside the face and eyes loop
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#destroys the program when Esc is hit
cam.release()
cv2.destroyAllWindows()
