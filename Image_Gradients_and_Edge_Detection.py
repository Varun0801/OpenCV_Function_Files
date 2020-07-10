# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:04:56 2020

@author: VARUN SAKUNIA
"""

#Image Gradient: It is the directional change in the intensity/color in an image

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\My_Face_DataSet\sudoku.jpg', cv2.IMREAD_GRAYSCALE)
#Laplasian method and converting into absolute values
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
#Parameters: img,dtype,dx,dy,ksize(optional)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
#Parameters: img,dtype,dy,dx,ksize(optional)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])