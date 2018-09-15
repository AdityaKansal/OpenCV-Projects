# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:07:38 2018

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

height,width = image.shape[:2]

T_y = height/4
T_x = width/4

T = np.float32([[1,0,T_x],[0,1,T_y]])


#warpAffine
image_transition = cv2.warpAffine(image,T,(width,height))
cv2.imshow('Transited Image',image_transition)
cv2.waitKey()

cv2.destroyAllWindows()