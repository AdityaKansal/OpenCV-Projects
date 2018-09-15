# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:00:33 2018

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
image = cv2.imread(path+'Desert.jpg')
cv2.imshow('Original Image',image)
cv2.waitKey()


#3/4 image - Linear Interpolation
image_scaled = cv2.resize(image,None,fx=0.75,fy=0.75)
cv2.imshow('Scaling-Linear Interpolation', image_scaled)
cv2.waitKey()

#double size of image
image_scaled = cv2.resize(image,None,fx=2,fy=2,interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling-Cubic Interpolation', image_scaled)
cv2.waitKey()


#skew and resizing
image_scaled = cv2.resize(image,(900,400),interpolation = cv2.INTER_CUBIC )
cv2.imshow('Scaling-INTER AREA Interpolation', image_scaled)
cv2.waitKey()

cv2.destroyAllWindows()