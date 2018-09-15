# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:12:39 2018

@author: akansal2
"""


#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#  Image
image = cv2.imread(path+'Sudoku.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,700,apertureSize = 3)

cv2.imshow('Sudoku_edges',edges)
cv2.waitKey()



lines = cv2.HoughLines(edges,1,np.pi/180,1)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b =np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    x2 = int(x0 - 1000*(-b))
    y1 = int(y0 +1000*(a))
    y2 = int(y0-1000*(a))
    cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)
    
    
cv2.imshow('Hough Lines',image)
cv2.waitKey()

    


#probablistic line image

#  Image
image = cv2.imread(path+'Sudoku.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,700,apertureSize = 3)


lines = cv2.HoughLinesP(edges,1,np.pi/180,280,5,10)
print(lines.shape)


for x1,y1,x2,y2 in lines[0]:
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
    
cv2.imshow('Probalistic Hough lines ',image)
cv2.waitKey()

cv2.destroyAllWindows()