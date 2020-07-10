# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:37:23 2020

@author: VARUN SAKUNIA
"""

import numpy as np
import cv2
#reading cascade file
face_cascade = cv2.CascadeClassifier('haarcascades_frontalface_default.xml')

img = cv2.imread('img.jpg', 1)

#detecting faces
faces = face_cascade.detectMultiscale(img, 1.3,4)
print(faces)

for (x,y,w,h) in faces:
    print(x,y,w,h)
    img = cv2.ectangle(img, (x,y), (x+w, y+h),(0,255,0),5)
    
resized = cv2.resize(img, (500,500))

cv2.imshow('')
    