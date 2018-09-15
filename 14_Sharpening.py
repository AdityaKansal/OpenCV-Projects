# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 08:53:48 2018

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

#creating our 3x3 kernel/filter
kernel = np.array([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]])
sharpened_image = cv2.filter2D(image,-1,kernel)
cv2.imshow('Sharpened Image',sharpened_image)
cv2.waitKey()

cv2.destroyAllWindows()