# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:06:48 2020

@author: VARUN SAKUNIA
"""

# Harris Corner Detection
"""
1. Determine which window produce very large variations in intensity
when moved in both X and Y directions
2. With each such window found, a score R is computed
3. After applying a threshold to this score, important corners are selected

"""

import numpy as np
import cv2 as cv

img = cv.imread(r"D:\My_Face_DataSet\shapes.png",1)

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Parameters: image(should be grayscale and float32 type), blocksize(window size-> size of neighbourhood considered for corner
# detection),ksize(Aparture parameter of Sobel Derivative used),k(Harris detector free parameter)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)

dst = cv.dilate(dst, None)

# reverting back to the original image with marking points with optimal threshold value
img[dst > 0.03 * dst.max()] = [0, 0, 255]

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()