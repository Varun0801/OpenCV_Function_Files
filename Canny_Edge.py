# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:54:42 2020

@author: VARUN SAKUNIA
"""

#Canny edge Detection is an edge detection operator that uses a multi-stage
#algorithm to detect a wide range of edges in images.

#It involved in 5 steps
# 1.Noise Reduction(Using GaussianFilter,etc.)
# 2. Gradient calculation(Finding Intensity Gradient)
# 3. Non-maximum supression(To get rid of spurious parts in images)
# 4. Double threshold(To determine the potential edges)
# Edge Tracking by Hysteresis(i.e, finalizing the detection of edges by supressing all weak/not connected edges )

import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(i):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('x', 'image', 0, 200, nothing)
cv2.createTrackbar('y', 'image', 0, 200, nothing)


while (1):
    img = cv2.imread(r'D:\My_Face_DataSet\sudoku.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    x = cv2.getTrackbarPos('x','image')
    y = cv2.getTrackbarPos('y','image')
    canny = cv2.Canny(img,x,y)
    cv2.imshow('Original',img)
    cv2.imshow('Edge-Detection',canny)
    k = cv2.waitKey(1)
    if (k==27):
        break
# =============================================================================
# 
#     titles = ['image', 'canny']
#     images = [img, canny]
#     for i in range(2):    
#         plt.subplot(1, 2, i+1), plt.imshow(images[i],'Gray')
#         plt.title(titles[i])
#         plt.xticks([]),plt.yticks([])
#         plt.show()  
# =============================================================================

cv2.destroyAllWindows()


# Comaring gradients with canny edge detection

# =============================================================================
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# 
# img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)
# lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
# lap = np.uint8(np.absolute(lap))
# sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
# sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
# edges = cv2.Canny(img,100,200)
# 
# sobelX = np.uint8(np.absolute(sobelX))
# sobelY = np.uint8(np.absolute(sobelY))
# 
# sobelCombined = cv2.bitwise_or(sobelX, sobelY)
# 
# titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']
# images = [img, lap, sobelX, sobelY, sobelCombined, edges]
# for i in range(6):
#     plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# 
# plt.show()
# =============================================================================
