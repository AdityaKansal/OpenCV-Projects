# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:44:24 2018

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



height, width = image.shape[:2]

#start
start_row = int(height*0.25)
start_col = int(width*0.25)

#end
end_row = int(height*0.75)
end_col = int(width*0.75)


cropped_image = image[start_row:end_row,start_col:end_col,:]
cv2.imshow('Cropped Image',cropped_image)
cv2.waitKey()

cv2.destroyAllWindows()