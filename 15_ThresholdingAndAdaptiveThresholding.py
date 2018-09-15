# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:21:54 2018

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

#converting a gray scale to its binary form
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray  Image',image)
cv2.waitKey()


#threshold
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()


ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()


ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()


ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()


ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()


#Adaptive Threshold
image = cv2.GaussianBlur(image,(3,3),0)

#adaptive mean
thresh1 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()

#Ostu threhold
_,thresh1 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()


#Ostu Threshold After Gaussian filtering
blur = cv2.GaussianBlur(image,(3,3),0)
_,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()






























cv2.destroyAllWindows()