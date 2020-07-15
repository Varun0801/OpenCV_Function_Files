# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:12:32 2020

@author: VARUN SAKUNIA
"""

import matplotlib.pylab as plt
import cv2
import numpy as np

image = cv2.imread(r"D:\My_Face_DataSet\road.jfif")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (-650, height),
    (width/2.6, height/2.10),
    (width+100, height)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

cropped_image = region_of_interest(image,
                np.array([region_of_interest_vertices], np.int32),)

plt.imshow(cropped_image)
plt.show()