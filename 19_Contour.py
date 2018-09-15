# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:36:33 2018

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
image = cv2.imread(path+'Penguins.jpg')
cv2.imshow('Original Image',image)
cv2.waitKey()


#gray scale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('blackWhite',gray)
cv2.waitKey()


#find canny edges
edges = cv2.Canny(gray,300,500)
cv2.imshow('edges',edges)
cv2.waitKey()


#finding contours
im2, contours,hierarchy= cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('changed edges',edges)
cv2.waitKey()

print(contours)

#drwaing contours
cv2.drawContours(image,contours,-1,(0,255,0),2)
cv2.imshow('Image with Contours',image)
cv2.waitKey()




































cv2.destroyAllWindows()
