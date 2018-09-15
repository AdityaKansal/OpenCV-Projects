# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 10:32:23 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#Image
image = cv2.imread(path+'Hydrangeas.jpg')
cv2.imshow('Original Image',image)
cv2.waitKey() 
#
#kernel
kernel = np.ones((5,5),np.uint8)


#now we erode
#removing pixels
erosion = cv2.erode(image,kernel,iterations=1)
cv2.imshow('Erosion Image',erosion)
cv2.waitKey()

#now dilation
#adding pixels
dilate = cv2.dilate(image,kernel,iterations=1)
cv2.imshow('Dilation Image',dilate)
cv2.waitKey()

#opening
#erosion follwed by dilation
opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
cv2.imshow('Open Image',opening)
cv2.waitKey()



#closing
#dilation follwed by erosion
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow('Close Image',closing)
cv2.waitKey()






cv2.destroyAllWindows()