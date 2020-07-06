# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:16:24 2020

@author: VARUN SAKUNIA
"""

import cv2

#for reading the video from camera 

cap = cv2.VideoCapture(0);

#.get() method is used to get the requirements from the image/video
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
#.CAP_PROP_FRAME_WIDTH has a no = 3 associated with it
#.CAP_PROP_FRAME_HEIGHT has a no = 4 associated with it
#.set is used to directly set the parametrs with using above lines of code

cap.set(3, 1580)
cap.set(4,700)
#even if higher resolution is provided it would output the available resolution 

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()