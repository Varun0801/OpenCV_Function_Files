# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:02:56 2020

@author: VARUN SAKUNIA
"""

import cv2
import numpy as np
 
img = cv2.imread(r'D:\My_Face_DataSet\varun.jpg',1)
#resizing the image
img = cv2.resize(img,(1000,900))
# drawing a line in the image

img = cv2.line (img, (0,0), (255,255), (0,255,0), 5)

# making arrowed line

img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0), 5 )

# we provide the image, coordinates of starting and ending point,color of the line,thickness as parameters

#making rectangle
img = cv2.rectangle(img, (100,200), (300,400), (0,0,255), 5)

# making rectangle filled 
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), -1)

# making a circle with centre coordinates and radius
img = cv2.circle(img, (447,500), 50, (0,255,0), 6) 

# putting text on the image with Parameters: img,text,starting point,font,font_size,colour,thickness,linetype
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'Varun Here',(42,450),font,5,(255,255,255),10,cv2.LINE_AA)

# creating a black image from numpy Parameters: Size,DType
img1 = np.zeros([512,512,3],np.uint8)

#other methods
#cv2.polylines()
#cv2.ellipse()

cv2.imshow('image1',img)
cv2.imshow('Black Image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()