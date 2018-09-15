# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 12:51:13 2018

@author: akansal2
"""



#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


# Template Image
image = cv2.imread(path+'CirclesAndEclipses.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('identifying Image',image)
cv2.waitKey()



#Blob Detector
detector = cv2.SimpleBlobDetector_create()


#Detect Blobs
keypoints = detector.detect(image)



#draw blobs on our image as red circles
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


number_of_blobs = len(keypoints)
text = 'Total number of blobs:' + str(len(keypoints))
cv2.putText(blobs,text,(20,550),cv2.FONT_HERSHEY_COMPLEX,1,(100,255,100),2)

cv2.imshow('With Blobs',blobs)
cv2.waitKey()




############################# only circles
params = cv2.SimpleBlobDetector_Params()



params.filterByArea = True
params.minArea = 100


params.filterByCircularity = True
params.minCircularity = 0.9


params.filterByConvexity = False
params.minConvexity = 0.2


params.filterByInertia = True
params.minInertiaRatio = 0.01



detector = cv2.SimpleBlobDetector_create(params)


#Detect Blobs
keypoints = detector.detect(image)



#draw blobs on our image as red circles
blank = np.zeros((1,1))
circles = cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


number_of_blobs = len(keypoints)
text = 'Total number of circles:' + str(len(keypoints))
cv2.putText(circles,text,(20,550),cv2.FONT_HERSHEY_COMPLEX,1,(100,255,100),2)

cv2.imshow('With circles',circles)
cv2.waitKey()



cv2.destroyAllWindows()