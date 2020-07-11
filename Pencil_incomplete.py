# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:42:50 2020

@author: VARUN SAKUNIA
"""

import cv2
img = cv2.imread(r'D:\My_Face_DataSet\varun.jpg',1)
cv2.resize(img,(800,600))
cv2.imshow('Original',img)

cartoon_image = cv2.stylization(img,sigma_s=150,sigma_r=0.25)
cv2.imshow('Cartoon',cartoon_image)

cartoon_image1 = cv2.pencilSketch(img,sigma_s=60,sigma_r=0.5,shade_factor = 0.02)
cv2.imshow('Pencil',cartoon_image1)

cv2.waitKey(0)
cv2.destroyAllWindows()