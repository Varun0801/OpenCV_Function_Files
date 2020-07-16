# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:59:08 2020

@author: VARUN SAKUNIA
"""

import numpy as np
import cv2 

img = cv2.imread(r"D:\My_Face_DataSet\smarties1.png",1)
output = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)

"""
circles = cv2.HoughCircles(image,method,dp,minDist[,circles[,param1[,param2[,minRadius[,maxRadius]]]]])

image: 8-bit,single channel,grayscale image
circles: Output vector of found circles
method: Detection method, see HoughModes.
dp: Inverse ratio of the accumulator resolution to the image resolution
minDist: Minimum distance between the centres of the detected circles
param1: First method-specific parameter.In case of HOUGH_GRADIENT, it is the higher threshold of the two 
        passed to the Canny edge detector(the lower one is twice smaller)
param2: Second method-specific parameter. In case of HOUGH_GRADIENT , it is the accumulator threshold for
        the circle centres at the detection stage.
minRadius: Minimum circle radius
maxRadius: Maximum circle radius. If <=0, uses the maximum image dimension. if < 0, returns centres without
           finding the radius
           
"""
circle = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=75,param2=30,minRadius=0,maxRadius=0)
detected_circles = np.uint16(np.round(circle))

for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(0,255,0),3)
    cv2.circle(output,(x,y),2,(255,255,0),3)


cv2.imshow('Output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
