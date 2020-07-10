# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:18:24 2020

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
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img,strXY, (x,y),font,0.5,(255,255,0),2)
        cv2.imshow('image',img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img,strBGR, (x,y),font,0.5,(0,255,255),2)
        cv2.imshow('image',img)
        

img = cv2.imread(r'D:\My_Face_DataSet\Template1.png',1)
#img = cv2.resize(img,(1000,900))
cv2.imshow('image',img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
        