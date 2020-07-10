# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:13:04 2020

@author: VARUN SAKUNIA
"""

#Homogeneous filter is the most simple filter,
#each output is the mean of its kernel neighbours

#In image processing a kernel,convolution matrix,or mask is a samll matrix 
#It is used for blugging,sharpening,embossing,edge detection,etc.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\My_Face_DataSet\water.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#defining kernel
kernel = np.ones((5,5),np.float32)/25
#parameters = img,desired_depth,kernel
dst = cv2.filter2D(img,-1,kernel)

# As in 1-D signals,images also can be filtered with various Low-Pass-Filters
# (LPF) for removing the noices and blurring the images and High-Pass-Filters(HPF)
# for finding edges in the images

blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)

#Median Filter replace each pixel's value with the median of its neighbouring pixels.
#Method works great when dealing with "Salt and pepper noise"
#kernel size must me odd always except 1
median = cv2.medianBlur(img,5)

# Parameters: img,diameter_around_image,sigmacolor,sigmaspace
bilateralFilter = cv2.bilateralFilter(img,9,75,75)
titles = ['image','2D Convolution','blur','GaussianBlur','MedianFilter','BilateralFilter']
images = [img,dst,blur,gblur,median,bilateralFilter]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()