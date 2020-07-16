# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:29:52 2020

@author: VARUN SAKUNIA
"""

import cv2
import matplotlib.pyplot as plt
    
img = cv2.imread(r'D:\My_Face_DataSet\home_final1.jpg',1)
img = cv2.resize(img,(680,1020))
print(img.shape)

font = cv2.FONT_HERSHEY_COMPLEX
name1 = "Burger"
img = cv2.putText(img,name1,(120,800),font,1.80,(0,0,255),3)
#cv2.imshow('Final',img)

font1 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
text = "50%Off" 
text2 = "Hurry up"
font2 = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img,text,(100,310),font1,2.25,(255,0,125),2)
img = cv2.putText(img,text2,(120,370),font2,1.50,(0,255,125),2)
#cv2.imshow('Final1',img)

font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
text3 = "Special Offers" 
text4 = "Awaiting for u only.."
font4 = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img,text3,(30,70),font3,2.20,(205,0,125),3)
img = cv2.putText(img,text4,(20,140),font4,1.25,(0,0,125),1)
#cv2.imshow('Final1',img)

font5 = cv2.FONT_HERSHEY_COMPLEX_SMALL
text5 = "-ON-"
img = cv2.putText(img,text5,(150,500),font5,2,(145,89,15),2)
#cv2.imshow('Final1',img)

food = cv2.imread(r'D:\My_Face_DataSet\burger.jpg',1)
print(food.shape)
food = cv2.resize(food,(300,250))
img[510:760,70:370] = food
#cv2.imshow('Food',img)


font6 = cv2.FONT_HERSHEY_COMPLEX_SMALL
font7 = cv2.FONT_HERSHEY_COMPLEX
text6 = "Contact us:"
text10 = "096178 83305" 
text7 = "Web: anshul@nanniz.com"
text8 = "Download our APP"
text9 = "Available for Android/IOS" 
img = cv2.putText(img,text10,(70,885),font7,1.25,(0,0,0),2)
img = cv2.putText(img,text6,(30,850),font7,0.75,(0,0,0),1)
img = cv2.putText(img,text7,(30,910),font6,1.20,(0,0,0),1)
img = cv2.putText(img,text8,(30,950),font7,1.25,(0,0,0),1)
img = cv2.putText(img,text9,(60,980),font6,1,(0,0,0),2)

img = cv2.rectangle(img,(25,825),(425,990),(49,69,59),2)
cv2.imshow('final',img)


cv2.waitKey(0)
cv2.destroyAllWindows()