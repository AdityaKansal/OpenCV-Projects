# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:27:49 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Rajiv Material/Master OpenCV/'


# Template Image
image = cv2.imread(path+'images/Trump.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('identifying Image',image)
cv2.waitKey()


#loading classifier
face_classifier = cv2.CascadeClassifier(path + 'Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier(path + 'Haarcascades/haarcascade_eye.xml')


#detecting faces
faces = face_classifier.detectMultiScale(gray,1.5,3)


#
if faces is ():
    print('No face found')
else:
    #drawing rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
        cv2.imshow('img',image)
        cv2.waitKey()
        #face is identified, now lets find eyes within that range
        face_color = image[y:y+h,x:x+w]
        face_gray = gray[y:y+h,x:x+w]
        eyes = eye_classifier.detectMultiScale(face_gray)
        for (ex,ey,eh,ew) in eyes:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
            cv2.imshow('img',image)
            cv2.waitKey()
            
cv2.destroyAllWindows()


def face_detector(img):
    #converting this image to gray
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is ():
        return img
    else:
        for (x,y,h,w) in faces:
            '''
            x = x-50
            w = w+50
            y = y-50
            h = h+50
            '''
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),5)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = img[y:y+h,x:x+w]
            
            eyes = eye_classifier.detectMultiScale(roi_gray)
            
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(127,255,0),2)
        
    img = cv2.flip(img,1)
    return img




cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow('Our face extractor',face_detector(frame))
    if cv2.waitKey(1) == 13:
        break
    
cap.release()
cv2.destroyAllWindows()

    





















