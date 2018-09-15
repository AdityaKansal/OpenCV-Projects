# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 13:28:52 2018

@author: akansal2
"""

#####################
#importing libraires
import cv2
import numpy as np
from matplotlib import pyplot as plt


#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Pictures/'


#Image
image = cv2.imread(path+'Desert.jpg')
#cv2.imshow('Coloured Image',image)
#cv2.waitKey()


histogram = cv2.calcHist([image],[2],None,[256],[0,256])

plt.hist(image.ravel(),256,[0,256])
plt.show()

color = ('b','g','r')

for i,col in enumerate(color):
    histogram2 = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color = col)
    plt.xlim([0,256])

plt.show()


#cv2.destroyAllWindows()