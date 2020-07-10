# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:52:56 2020

@author: VARUN SAKUNIA
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier("D:\OpenCV\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

eye_detector = cv2.CascadeClassifier("D:\OpenCV\opencv-master\data\haarcascades\haarcascade_eye.xml")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = np.uint8(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.4, 5)

    for (x,y,w,h) in faces:

        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        face_bw = gray[y:y+h, x:x+w]

        face_color = frame[y:y+h, x:x+w]

        eyes = eye_detector.detectMultiScale(face_bw)

        for (ex,ey,ew,eh) in eyes:
            
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    # Display the resulting frame
    #cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('Detected frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()