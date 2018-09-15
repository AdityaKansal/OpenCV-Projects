# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 12:10:35 2018

@author: akansal2
"""

#importing libraries
import cv2
import numpy as np


def image_processor(image):
    # Black and white image
    processed_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    #Clean up image using Gaussian blur
    processed_image = cv2.GaussianBlur(processed_image,(5,5),0)
    
    #Finding edges using canny
    processed_image = cv2.Canny(processed_image,10,70)
    
    #Do an invert binarize the image
    ret,processed_image = cv2.threshold(processed_image,70,255,cv2.THRESH_BINARY_INV)
    
    return processed_image

#object for webcam
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()  #ret for boolean if image is there, frame is image captured
    cv2.imshow('Live Sketcher',image_processor(frame))
    if cv2.waitKey(1) == 13:   #13 for enter
        break
    
    
cap.release()
cv2.destroyAllWindows()
    



