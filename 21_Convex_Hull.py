# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:12:51 2018

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
image = cv2.imread(path+'House.png')
cv2.imshow('Original Image',image)
cv2.waitKey()

#keeping a copy
orig_image = image.copy()

#grayscale and Binarize
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Thresh Image',thresh)
#cv2.waitKey()

#find contours
im2,contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


#iterate thru each contour and find bounding rectangle
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(orig_image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Bounding rectangle ',orig_image)
    
cv2.waitKey()


#iterate thru each contour and compute the approx contour
for c in contours:
    #compute accuracy as percentage of permiter of contour
    accuracy = 0.03*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,accuracy,True)
    cv2.drawContours(image,[approx],0,(0,255,0),2)
    cv2.imshow('Approx Poly DP',image)
    
    
cv2.waitKey()
    

#convex hull - Smallest polygon that can fit the image - Similar to bounding rectangle

#Image
image = cv2.imread(path+'Hand.png')
cv2.imshow('Original hand Image',image)
cv2.waitKey()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#Threshold image
ret,thresh = cv2.threshold(gray,176,255,0)

#find Contours
_,contours,heirarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

#Sort contours based on area and remove the largest frame
n =len(contours) -1
contours = sorted(contours,key = cv2.contourArea,reverse = False)[:n]


#iterate thru contours and draw the convex hull
for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image,[hull],0,(0.255,0),2)
    cv2.imshow('Convex Hull',image)
    
cv2.waitKey()


cv2.destroyAllWindows()