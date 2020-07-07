# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:04:52 2020

@author: VARUN SAKUNIA
"""

import cv2
import datetime

#for reading the video from camera 

cap = cv2.VideoCapture(0);


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        
        #putting text on Video
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' ' +'Height: ' + str(cap.get(4))
        
        date_time = str(datetime.datetime.now())
        
        #Parameters : frame,text,Coordinates,font_type,font_scale,color,thickness,linetype
        
        frame = cv2.putText(frame,date_time + '  '+ text, (10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        
        cv2.imshow('frame', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()