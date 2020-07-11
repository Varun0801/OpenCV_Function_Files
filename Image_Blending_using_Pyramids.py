# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:49:49 2020

@author: VARUN SAKUNIA
"""

import cv2
import numpy as np
apple = cv2.imread(r'D:\My_Face_DataSet\apple1.png')
apple = cv2.resize(apple,(512,512))
orange = cv2.imread(r'D:\My_Face_DataSet\orange1.png')
orange = cv2.resize(orange,(512,512))
print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:,:256],orange[:,256:]))

# Image Blending : To remove the line of separation of two images
# Steps:1. Load the two images,
#       2. find the Gaussian Pyramids for both the images(here no. of levels is 6)
#       3. From Gaussian Pyramids, find their Laplacian Pyramids
#       4. Now join the left half of 1st image and the right half of 2nd image in each levels of Laplacian pyramids
#       5. Finally from this joint image pyramids, reconstruct yhe original image

# genetare Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


# generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate Laplacian Pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

# generate Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
# now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()