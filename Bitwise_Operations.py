# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:21:35 2020

@author: VARUN SAKUNIA
"""

import cv2
import numpy as np

# size of images must be same
#img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.imread(r'D:\My_Face_DataSet\varun.jpg')
img1 = cv2.resize(img1,(800,600))
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread(r'D:\My_Face_DataSet\varun1.jpg')
img2 = cv2.resize(img2,(800,600))

# performing logical AND,OR,XOR,NOT
bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()

