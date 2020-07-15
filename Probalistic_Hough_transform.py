# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:01:03 2020

@author: VARUN SAKUNIA
"""

import cv2
import numpy as np
img = cv2.imread(r"D:\My_Face_DataSet\Sudoku.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,200,apertureSize = 3)
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,75,minLineLength=75,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
"""
lines=cv.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]])

rho : Distance resolution of the accumulator in pixels.

theta: Angle resolution of the accumulator in radians.

threshold:Accumulator threshold parameter. Only those lines are returned that get enough votes ( greater then threshold ).

minLineLength : Minimum length of line. Line segments shorter than this are rejected.
maxLineGap  : Maximum allowed gap between line segments to treat them as a single line.
"""