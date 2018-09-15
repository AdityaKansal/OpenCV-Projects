# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:25:15 2018

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

rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),180,1)
rotated_image = cv2.warpAffine(image,rotation_matrix,(width,height))
cv2.imshow('Rotated image',rotated_image)
cv2.waitKey()


#taking transpose
transposed_image = cv2.transpose(rotated_image)
cv2.imshow('Transpose Image',transposed_image)
cv2.waitKey()

cv2.destroyAllWindows()
