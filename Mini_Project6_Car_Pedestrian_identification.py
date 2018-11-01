# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:40:35 2018

@author: akansal2
"""


#importing libraires
import cv2
import numpy as np
import time



import sys
print(sys.executable)

#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Rajiv Material/Master OpenCV/'


#create our body classifier
body_classifier = cv2.CascadeClassifier(path + 'Haarcascades\haarcascade_fullbody.xml')


#inititate the video capture
cap = cv2.VideoCapture(path + 'images/walking.avi')


while cap.isOpened():
    
    #read first frame
    ret,frame = cap.read()
    frame = cv2.resize(frame,None,fx = 0.5,fy =0.5,interpolation = cv2.INTER_LINEAR)
     
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #pass frame to body classifier
    bodies = body_classifier.detectMultiScale(gray,1.2,3)
    
    
    #bounding box
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('Pedesterians',frame)
        
        
    if cv2.waitKey(1) == 13:
        break
    
cap.release()
cv2.destroyAllWindows()



#detecting cars
car_classifier = cv2.CascadeClassifier(path + 'Haarcascades\haarcascade_car.xml')

print('1')
cap1 = cv2.VideoCapture(path + 'images/cars.avi')
print('2')

while cap1.isOpened():
    
    #time.sleep(0.05)
    print('3')
    #read first frame
    ret,frame = cap1.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #pass frame to our class classifier
    cars = car_classifier.detectMultiScale(gray,1.4,2)
    
    
    #bounding box
    for (x,y,w,h) in cars:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
         cv2.imshow('Cars',frame)
         
         
    if cv2.waitKey(1) == 13:
        break
     
print('4')        
cap1.release()
cv2.destroyAllWindows()
         

        
    















        
        
        
        
        
    
