# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:06:05 2018

@author: akansal2
"""

# a blob is group of pixels that share common property

#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#  Image
image = cv2.imread(path+'Sunflowers.jpg',cv2.IMREAD_GRAYSCALE)
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,100,700,apertureSize = 3)

cv2.imshow('original',image)
cv2.waitKey()


detector = cv2.SimpleBlobDetector_create()

keypoint = detector.detect(image)


blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image,keypoint,blank,(0,255,255),cv2.DRAW_MATCHES_FLAGS_DEFAULT)


cv2.imshow('BLOBS',blobs)
cv2.waitKey()


cv2.destroyAllWindows()