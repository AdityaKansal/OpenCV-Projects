# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:52:08 2018

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
image = cv2.imread(path+'Chess.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('identifying Image',image)
cv2.waitKey()



#changing gray to float32 format
gray = np.float32(gray)


#harris corner
harris_corners = cv2.cornerHarris(gray,3,3,0.05)


kernel = np.ones((7,7),np.uint8)
harris_corners = cv2.dilate(harris_corners,kernel, iterations = 2)


image[harris_corners > 0.025*harris_corners.max()] = [0,0,127]


cv2.imshow('Harris Corners',image)
cv2.waitKey()




#good features to track
image = cv2.imread(path+'Chess.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray,40,0.01,15)



for corner in corners:
    x,y = corner[0]
    x = int(x)
    y = int(y)
    cv2.rectangle(image,(x-10,y-10),(x+10,y+10),(0,255,0),2)
    
    
cv2.imshow('Corners found',image)
cv2.waitKey()
    


cv2.destroyAllWindows()