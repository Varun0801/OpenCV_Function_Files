# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:02:30 2020

@author: VARUN SAKUNIA
"""


import cv2
import numpy as np

# for getting all the events available in cv2 library

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# creating a mouse callback function which is executed when mouse event takes place
 
def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #making a point in the image
        
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        
        #joining the new created and last created points
        
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
        cv2.imshow('image',img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img,(x,y),3,(0,255,0),-1)
        
        #making a separate window for displaying colours
        myimg = np.zeros((512,512,3),np.uint8)
        myimg[:] = [blue,green,red]
        cv2.imshow('Colour_Window',myimg)
        
img = cv2.imread(r'D:\My_Face_DataSet\varun.jpg',1)

img = cv2.resize(img,(1000,900))
cv2.imshow('image',img)

points = []


cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()