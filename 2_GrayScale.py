# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:55:35 2018

@author: akansal2
"""

#####################
#importing libraires
import cv2
import numpy as np


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#Image
image = cv2.imread(path+'Desert.jpg')
cv2.imshow('Coloured Image',image)
cv2.waitKey()

#Gray Scale Image
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',gray_image)
cv2.waitKey()
cv2.destroyAllWindows()

###########################################
#short way
gray_image = cv2.imread(path + 'Desert.jpg',0)
cv2.imshow('Gray Image',gray_image)
cv2.waitKey()
cv2.destroyAllWindows()


image.shape
gray_image.shape


