# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:07:41 2020

@author: VARUN SAKUNIA
"""

import numpy as np
import cv2
# to create a black screen
img = np.zeros((512,512,3), np.uint8)
# draw a rectangular box
cv2.rectangle(img, (200,100), (300,0), (255,0,255), 5)
# cv2.rectangle(img, (200,300), (300,100), (255,0,255), 5)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()