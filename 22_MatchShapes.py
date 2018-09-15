# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:28:16 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


# Template Image
template = cv2.imread(path+'Template.png')
template_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
cv2.imshow('Template Image',template)
cv2.waitKey()



#Target Image
target = cv2.imread(path+'ContoursImages.png')
#cv2.imshow('Target Image',target)
#cv2.waitKey()

target_gray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)



#Threshold both images
ret1,thresh1 = cv2.threshold(template_gray,127,255,0)
ret2,thresh2 = cv2.threshold(target_gray,127,255,0)


#find contours in template
im2,contours,heirarchy = cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)



#sorted countours
sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)


#Taking the second largest contour. as first one would be the image outline itself
template_contour = sorted_contours[1]


#extract contours from the target image
im3,contours,hierarchy = cv2.findContours(thresh2,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i,c in enumerate(contours):
    print(i)
    match = cv2.matchShapes(template_contour,c,1,0.0)
    print(match)
    if match < 0.18:
        closed_contour = c
    else:
        closed_contour = []

        
cv2.drawContours(target,[closed_contour],-1,(0,255,0),3)
cv2.imshow('Output',target)
cv2.waitKey()



































cv2.destroyAllWindows()
