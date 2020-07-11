# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:32:47 2020

@author: VARUN SAKUNIA
"""

# Pyramid or Pyramid Representation is a type of multi scale signal representation in which a singal
# or an image is subject to repeated smoothing and resubsampling

# 2 Types of Pyramid: 1. Gaussian Pyramid  ,2. Laplasian Pyramid
# Gaussian Pyramid: Repeat Filtering and Subsampling , Functions: Pyred Down and Pyred Up
# Laplacian Pyramid : No exclusive method, A level of Laplacian Pyramid is formed by the diffrence between
# that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid

# Both the pyramids help us to blend the images and reconstruction of the images

import cv2
import numpy as np

img = cv2.imread(r'D:\My_Face_DataSet\varun.jpg') 
#img = cv2.resize(img,(800,600))

# Demonstrating Gaussian Pyramid one by one
# =============================================================================
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# lr3 = cv2.pyrDown(lr2)
# hr1 = cv2.pyrUp(img)
# hr2 = cv2.pyrUp(hr1)
# hr3 = cv2.pyrUp(hr2)
# 
# 
# cv2.imshow("Original Image",img)
# cv2.imshow("PyrDown 1st reduced Image",lr1)
# cv2.imshow("PyrDown 2nd reduced Image",lr2)
# cv2.imshow("PyrDown 3rd reduced Image",lr3)
# cv2.imshow("PyrUp 1st increased Image",hr1)
# cv2.imshow("PyrUp 2nd increased Image",hr2)
# cv2.imshow("PyrUp 3rd increased Image",hr3)
# =============================================================================


# Demonstrating Gaussian Pyramid Array
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

# Demonstrating Laplacian Pyramid
layer = gp[5]
cv2.imshow('Upper level Gaussian Pyramid',layer)
lp = [layer]
for i in range(5,0,-1): 
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)
     
cv2.waitKey(0)
cv2.destroyAllWindows()