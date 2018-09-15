# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:59:03 2018

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


#matrix
M = np.ones(image.shape,np.uint8)*75

#addition
added = cv2.add(image,M)
cv2.imshow('Added',added)
cv2.waitKey()


#subtraction
subtracted = cv2.subtract(image,M)
cv2.imshow('Subtracted',subtracted)
cv2.waitKey()
cv2.destroyAllWindows()

#loop
N = np.ones(image.shape,np.uint8)*10
for i in range(10):
    image = cv2.add(image,N)
    cv2.imshow('Added',image)
    cv2.waitKey()

    



cv2.destroyAllWindows()