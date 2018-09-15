# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:59:45 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'

print(cv2.__version__)

# Template Image
image = cv2.imread(path+'Lighthouse.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('identifying Image',image)
cv2.waitKey()



#SIFT
sift = cv2.SIFT()
# SIFT SURF not available for OpenCV 3+




cv2.destroyAllWindows()
