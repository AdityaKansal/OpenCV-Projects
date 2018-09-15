# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 16:21:14 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#Creating a black Image
image = np.zeros((512,512,3),np.uint8)
cv2.imshow('Image',image)
cv2.waitKey()

image_bw = np.zeros((512,512),np.uint8)
cv2.imshow('bw image',image_bw)
cv2.waitKey()



#drawing a line
image = np.zeros((512,512,3),np.uint8)
cv2.line(image,(0,0),(170,170),(0,0,255),5)
cv2.imshow('Red line',image)
cv2.waitKey()


#drwaing a rectangle
image = np.zeros((512,512,3),np.uint8)
cv2.rectangle(image,(100,100),(240,240),(100,100,1),5)
cv2.imshow('Rectabgle',image)
cv2.waitKey()


#drwaing a circle
image = np.zeros((512,512,3),np.uint8)
cv2.circle(image,(200,200),100,(15,75,50),10)
cv2.imshow('Circle',image)
cv2.waitKey()



#drwaing a polygon
image = np.zeros((512,512,3),np.uint8)
pts = np.array([[10,50],[12,30],[70,30],[100,100],[250,140]],np.int32)
pts = pts.reshape((-1,1,2))

cv2.polylines(image,[pts],True,(0,0,255),3)
cv2.imshow('Polygon',image)
cv2.waitKey()






#text on image
image = np.zeros((512,512,3),np.uint8)
cv2.putText(image,'Hello World',(100,250),cv2.FONT_ITALIC,2,(0,255,0),2)
cv2.imshow('Hello World',image)
cv2.waitKey()

cv2.destroyAllWindows()