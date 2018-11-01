# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:00:38 2018

@author: akansal2
"""
import dlib
import numpy as np
import cv2


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Rajiv Material/Master OpenCV/'


PREDICTOR_PATH = path + 'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(PREDICTOR_PATH)
detector = dlib.get_frontal_face_detector()


class TooManyFaces(Exception):
    pass

class NoFaces(Exception):
    pass

def get_landmarks(im):
    rects = detector(im,1)
    
    if len(rects) > 1:
        raise TooManyFaces
        
    if len(rects)==0:
        raise NoFaces
    
    return np.matrix([[p.x,p.y] for p in predictor(im,rects[0]).parts()])
        
    
def annotate_landmarks(im,landmarks):
    im = im.copy()
    for idx,point in enumerate(landmarks):
        pos = (point[0,0],point[0,1])
        cv2.putText(im,str(idx),pos,fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.4,color = (0,0,255))
        cv2.circle(im,pos,3,color = (0,255,255))    
    return im
    
    
image = cv2.imread(path + 'images/Vani.jpg')
landmarks = get_landmarks(image)
image_with_landmarks = annotate_landmarks(image,landmarks)

cv2.imshow('Image with landmarks',image_with_landmarks)
cv2.waitKey()
cv2.destroyAllWindows()










