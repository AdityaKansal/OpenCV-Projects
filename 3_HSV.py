# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:42:45 2018

@author: akansal2
"""

#####################
#importing libraires
import cv2
import numpy as np


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#Image
image = cv2.imread(path+'Desert.jpg')
cv2.imshow('Coloured Image',image)
cv2.waitKey()


#image shape for BGR
image.shape
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_image.shape


image[0][0][:]

gray_image[0][0]



#BGRR to HSV
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv_image',hsv_image)
cv2.waitKey()

'''
cv2.imshow('Hue Channel',hsv_image[:][:][0])
cv2.waitKey()
cv2.imshow('Saturation Channel',hsv_image[:][:][1])
cv2.waitKey()
cv2.imshow('Value Channel',hsv_image[:][:][2])
cv2.waitKey()
'''

'''
###########################
#splitting image into R G B
cv2.imshow('Red Channel',image[:][:][0])
cv2.waitKey()
cv2.imshow('Green Channel',image[:][:][1])
cv2.waitKey()
cv2.imshow('Blue Channel',image[:][:][2])
cv2.waitKey()
'''

#image split
B,G,R = cv2.split(image)

cv2.imshow('Red Channel',R)
cv2.waitKey()
cv2.imshow('Green Channel',G)
cv2.waitKey()
cv2.imshow('Blue Channel',B)
cv2.waitKey()


Merged = cv2.merge([B,G,R])
cv2.imshow('Merged image',Merged)
cv2.waitKey()


Blue_amplify = cv2.merge([B+100,G,R])
cv2.imshow('Merged Blue Amplify image',Blue_amplify)
cv2.waitKey()



# RGB effects
B,G,R = cv2.split(image)

zeroes = np.zeros(image.shape[:2],dtype = 'uint8')
cv2.imshow('zero image',zeroes)
cv2.imshow('Red image',cv2.merge([zeroes,zeroes,R]))
cv2.waitKey()

cv2.imshow('Green image',cv2.merge([zeroes,G,zeroes]))
cv2.waitKey()

cv2.imshow('Blue image',cv2.merge([B,zeroes,zeroes]))
cv2.waitKey()




cv2.destroyAllWindows()

