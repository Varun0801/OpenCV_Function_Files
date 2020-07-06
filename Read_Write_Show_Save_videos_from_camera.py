# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:28:58 2020

@author: VARUN SAKUNIA
"""

import cv2

#for reading the video from camera 

cap = cv2.VideoCapture(0);

#for saving the capture we create a videowriter class

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

# we specify output_file name, fourcc code, FramesPerSecond, size of frame

print(cap.isOpened()) 

#To check if the file/video is opening or not

while (cap.isOpened()):
    ret,frame = cap.read()
    
    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
        #.get() method is used to get the requirements from the image/video
    
        #writing the file
        
        out.write(frame)
        # we save the file in BGR format
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()