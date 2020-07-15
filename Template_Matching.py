# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:23:44 2020

@author: VARUN SAKUNIA
"""

import cv2
import numpy as np
img = cv2.imread(r"D:\My_Face_DataSet\varun12.jpg",1)
#img = cv2.resize(img,(800,800))
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#applying template matching
template = cv2.imread(r"D:\My_Face_DataSet\varun12.1.jpg", 0)
w, h = template.shape[::-1]

#getting all the matchings
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED )
print(res)
#applying threshold
threshold = 0.99;
loc = np.where(res >= threshold)
print(loc)
#making the matching bounding to the maximum coordinates for bounding boxes
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()