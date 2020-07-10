# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:18:42 2020

@author: VARUN SAKUNIA
"""

import cv2

img1 = cv2.imread(r'D:\My_Face_DataSet\varun.jpg',1)
img1 = cv2.resize(img1,(512,512))

img2 = cv2.imread(r'D:\My_Face_DataSet\lion.jpg',1)
img2 = cv2.resize(img2,(512,512))

# returning a tuple of number of rows, columns, and channels 
print(img1.shape)

# returning total number of pixels accessed
print(img1.size)

# returning image datatype 
print(img1.dtype)

#Splitting img into 3 channels
b,g,r = cv2.split(img1)
#cv2.imshow('Blue Channel',b)
#cv2.imshow('Green Channel',g)
#cv2.imshow('Red Channel',r)

# Merging color channels
img1 = cv2.merge((b,g,r))

# ROI finding and again appending it on image 
eye = img1[541:303,622:304]
img1[610:333,600:350] = eye

# adding two images,(should be of same size)
add_img = cv2.add(img2,img1)
cv2.imshow('Merged',add_img)

# adding two images in terms of weight
add_img1 = cv2.addWeighted(img1,.6,img2,.4,1);
cv2.imshow('Merged1',add_img1)


cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
