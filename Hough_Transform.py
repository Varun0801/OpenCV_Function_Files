# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:32:27 2020

@author: VARUN SAKUNIA
"""

# Hough Trandsform: The Hough Transform is a popular technique to 
# detect any shape, if you can represent that shape in a mathematical 
# form.It can detect the shape even if it is broken or distorted a little bit

# Hough Transform Basics : A line in the image space can be expressed with two 
# varaibles. For ex: In the Cartesian coordinate system y1 = mx1 + c, In the Polar 
# coordinate system xcos0 + ysin0 = r 

# we have Hough Space which has m along the x-axis and c along the y-axis of y = mx + c eqn and its representing 
# the same line with a point which is very easy to handle and if any point(x,y) is represented in XY plane then it 
# can also be represented in MC space with c = xm + y with slope=-x and intercept = y

# Hough transform is all about converting points in XY plane to the lines in MC space or Huff space
# Line representation in Hough space is r = xcos0 + ysin0

# Hough Transformation Algorithm
# 1.Edge Detection,e.g. using the canny edge detector
# 2.Mapping of edge points to the Hough space and storage in an accumulator
# 3.Interpretation of the accumulator to yield lines of infinite length. 
#    The interpretation is done by thresholding and possibly other constraints
# 4.Conversion of infinite lines to finite lines

# two kinds of Hough Line Transforms : 1.The Standard Hough Transform(HoughLines method)
# 2. The Probabilistic Hough Line Transform(HoughLinesP method)

#cv2.HoughLines(image, rho, theta, threshold) 
import cv2
import numpy as np

img = cv2.imread(r"D:\My_Face_DataSet\Sudoku.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 150, 250, apertureSize=3)
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 230)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()