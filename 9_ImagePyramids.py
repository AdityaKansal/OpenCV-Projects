# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:39:10 2018

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

Smaller = cv2.pyrDown(image)
cv2.imshow('Smaller Image',Smaller)
cv2.waitKey()

Smaller = cv2.pyrDown(Smaller)
cv2.imshow('Smaller Image',Smaller)
cv2.waitKey()

Larger = cv2.pyrUp(Smaller)
cv2.imshow('Larger Image',Larger)
cv2.waitKey()


Larger = cv2.pyrUp(Larger)
cv2.imshow('Larger Image',Larger)
cv2.waitKey()

cv2.destroyAllWindows()

