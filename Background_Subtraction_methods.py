# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:29:29 2020

@author: VARUN SAKUNIA
"""

import numpy as np
import cv2 
cap = cv2.VideoCapture("walk1.mp4")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.BackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
#fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv2.destroyAllWindows()