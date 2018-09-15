# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 16:49:26 2018

@author: akansal2
"""

#####################
#importing libraires
import cv2

import numpy as np

#displaying a pic
input = cv2.imread('C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/Desert.jpg')
cv2.imshow('hello',input)
cv2.waitKey()
cv2.destroyAllWindows()



#input parameters
input.shape   #768,1024,3



#saving the edited file
cv2.imwrite('C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/Desert2.jpg',input)
