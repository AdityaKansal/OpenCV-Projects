# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:23:58 2018

@author: akansal2
"""



#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#  Image
image = cv2.imread(path+'Coins.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,100,700,apertureSize = 3)

cv2.imshow('gray',gray)
cv2.waitKey()



blur = cv2.medianBlur(gray,5)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1.5,50)

for i in circles[0,:]:
    cv2.circle(image,(i[0],i[1]),i[2],(255,0,0),2)
    cv2.circle(image,(i[0],i[1]),2,(0,255,0),5)
    
    
            
    

cv2.imshow('Coins_edges',image)
cv2.waitKey()



cv2.destroyAllWindows()
