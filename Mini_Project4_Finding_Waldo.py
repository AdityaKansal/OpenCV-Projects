# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:14:58 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


# Template Image
image = cv2.imread(path+'WhereIsWaldo.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('identifying Image',image)
cv2.waitKey()


#Load Template Image
template = cv2.imread(path+'Waldo3.jpg',0)


#matching
result = cv2.matchTemplate(gray,template,cv2.TM_CCORR_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)


#creating Bounding box
top_left = max_loc
bottom_right = (top_left[0] +50,top_left[1]+50)
cv2.rectangle(image,top_left,bottom_right,(0,0,255),5)

cv2.imshow('Where is Waldo',image)
cv2.waitKey()


cv2.destroyAllWindows()


