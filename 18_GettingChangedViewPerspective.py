# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 11:42:35 2018

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

row,col,ch = image.shape

#4 coordinates of original image
points_A = np.float32([[320,15],[700,215],[85,610],[530,780]])

# 4 coordinates of new image
points_B = np.float32([[0,0],[420,0],[0,594],[420,594]])

#The perspective Transfomration Matrix
M = cv2.getPerspectiveTransform(points_A,points_B)

warped = cv2.warpPerspective(image,M,(420,594))
cv2.imshow('Changed Image',warped)
cv2.waitKey()



#affine 

#3 coordinates of original image
points_C = np.float32([[320,15],[700,215],[85,610]])

# 3 coordinates of new image
points_D = np.float32([[0,0],[420,0],[0,594]])



M =cv2.getAffineTransform(points_C,points_D)
warped = cv2.warpAffine(image,M,(col,row))
cv2.imshow('Affined Image',warped)
cv2.waitKey()





cv2.destroyAllWindows() 

