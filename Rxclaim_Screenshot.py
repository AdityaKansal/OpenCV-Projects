# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 18:51:40 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt
try:
    import Image
except ImportError:
    from PIL import Image
    
import pytesseract


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#Image
image = cv2.imread(path+'RxClaim.png')
cv2.imshow('Original Image',image)
cv2.waitKey() 


#b/w
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image',image)
cv2.waitKey() 



#threshold
ret,thresh1 = cv2.threshold(image,200,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold Image',thresh1)
cv2.waitKey()
#
##Sobel - Vertical and horizontal images
#sobel_x = cv2.Sobel(image,cv2.CV_64F,0,1,ksize =5)
#sobel_y = cv2.Sobel(image,cv2.CV_64F,1,0,ksize =5)
#
#cv2.imshow('Horizontal axis',sobel_x)
#cv2.waitKey()
#
#
#cv2.imshow('Verical axis',sobel_y)
#cv2.waitKey()
#
#
##sobel horizontal + vertical
#combine = cv2.bitwise_or(sobel_x,sobel_y)
#cv2.imshow('Both axis',combine)
#cv2.waitKey()
#

result = pytesseract.image_to_string(Image.open(path+'RxClaim.png'))

print(result)
cv2.destroyAllWindows()