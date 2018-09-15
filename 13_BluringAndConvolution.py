# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 07:13:08 2018

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
kernel = np.ones((3,3),np.float32)/9

#blurred 
blurred = cv2.filter2D(image,-1,kernel)
cv2.imshow('Blurred Image',blurred)
cv2.waitKey()



#7x7 filter
kernel = np.ones((7,7),np.float32)/49
#blurred 
blurred = cv2.filter2D(image,-1,kernel)
cv2.imshow('Blurred Image',blurred)
cv2.waitKey()





#Average Blur
blur = cv2.blur(image,(3,3))
cv2.imshow('Average Blur',blur)
cv2.waitKey()


#Gaussian blur
blur = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Gaussian Blur',blur)
cv2.waitKey()


#Median Blur
blur = cv2.medianBlur(image,5)
cv2.imshow('Median Blur',blur)
cv2.waitKey()


#Bilateral Blur - keeps the edges
blur = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('Bilateral Blur',blur)
cv2.waitKey()



#image de noising
dst = cv2.fastNlMeansDenoisingColored(image,None,6,6,7,21)
cv2.imshow('Noise removal',dst)
cv2.waitKey()






















cv2.destroyAllWindows()




















