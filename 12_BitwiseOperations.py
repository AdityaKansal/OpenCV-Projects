# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 21:08:13 2018

@author: akansal2
"""

#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#making a square
square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(200,200),255,-5)
cv2.imshow('Square',square)
cv2.waitKey()


#making a elipse
ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow('Ellipse',ellipse)
cv2.waitKey()




#bitwise OR
bitwise_or = cv2.bitwise_or(square,ellipse)
cv2.imshow('OR',bitwise_or)
cv2.waitKey()



#bitwise AND
bitwise_and = cv2.bitwise_and(square,ellipse)
cv2.imshow('AND',bitwise_and)
cv2.waitKey()



#bitwise XOR
bitwise_xor = cv2.bitwise_xor(square,ellipse)
cv2.imshow('XOR',bitwise_xor)
cv2.waitKey()



#bitwise NOT
bitwise_not = cv2.bitwise_not(ellipse)
cv2.imshow('NOT',bitwise_not)
cv2.waitKey()



cv2.destroyAllWindows()
