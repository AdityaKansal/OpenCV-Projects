# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 11:15:19 2018

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



#Sobel - Vertical and horizontal images
sobel_x = cv2.Sobel(image,cv2.CV_64F,0,1,ksize =5)
sobel_y = cv2.Sobel(image,cv2.CV_64F,1,0,ksize =5)

cv2.imshow('Horizontal axis',sobel_x)
cv2.waitKey()


cv2.imshow('Verical axis',sobel_y)
cv2.waitKey()


#sobel horizontal + vertical
combine = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Both axis',combine)
cv2.waitKey()



#Laplacian - Gets all Orientation
laplacian = cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow('Laplacian',laplacian)
cv2.waitKey()


#Canny
canny = cv2.Canny(image,20,170)
cv2.imshow('Canny image',canny)
cv2.waitKey()




cv2.destroyAllWindows()