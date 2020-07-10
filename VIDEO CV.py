# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:51:29 2020

@author: VARUN SAKUNIA
"""

import cv2
cap = cv2.VideoCapture("C:/Users/VARUN SAKUNIA/Downloads/BirdNoSound.mp4")

while(True):
    #capture frame-frame
    ret, frame = cap.read()
    
    #display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(25)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()