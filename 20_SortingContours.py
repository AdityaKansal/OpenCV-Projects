# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:26:10 2018

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
image = cv2.imread(path+'Contours_Sort.png')
cv2.imshow('Original Image',image)
cv2.waitKey()




#create a blank image with same dimension as our loaded image
blank_image = np.zeros((image.shape[0],image.shape[1],image.shape[2]),dtype = np.uint8)
#cv2.imshow('BLANK Image',blank_image)
#cv2.waitKey()


#create a copy of original image
original_image = image




#gray scale our image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray Image',gray)
#cv2.waitKey()



#find canny images
edged = cv2.Canny(gray,50,200)
cv2.imshow('canny Image',edged)
cv2.waitKey()

#find contours
_,contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


#draw contours
cv2.drawContours(blank_image,contours,-1,(0,255,0),3)
cv2.imshow('All contours over blank image',blank_image)
cv2.waitKey()

def get_contours_areas(contours):
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

#contours area before sort 
print(get_contours_areas(contours))

#sort contours large to small
sorted_contours = sorted(contours,key = cv2.contourArea,reverse = True)

#contour area after sort
print(get_contours_areas(sorted_contours)) 



#drawing contours
for c in sorted_contours:
    cv2.drawContours(original_image,[c],-1,(0,255,0),3)
    cv2.imshow('Contours by area',original_image)
    cv2.waitKey()
    

cv2.waitKey()
cv2.destroyAllWindows()



###sorting from left to right

#Image
image = cv2.imread(path+'Contours_Sort.png')
original_image = image.copy()



#compute centroids and draw them on our image
def label_contour_center(image,c,i):
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    
    #draw a circle at that centroid
    cv2.circle(image,(cx,cy),10,(0,0,255),-1)
    return image
    
    
    
    
for i,c in enumerate(contours):
    orig = label_contour_center(image,c,i)
    

cv2.imshow('Contour centers',orig)
cv2.waitKey()



#sorting contours from left to right
def x_cord_contours(contours):
    if cv2.contourArea(contours) > 10:    
        M = cv2.moments(contours)
        cx = int(M['m10']/M['m00'])
        return cx
        

contours_left_to_right = sorted(contours,key = x_cord_contours,reverse = False)

print(get_contours_areas(contours_left_to_right))

#Labelling contours left to right
for i,c in enumerate(contours_left_to_right):
    cv2.drawContours(original_image,[c],-1,(0,0,255),3)
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.putText(original_image,str(i+1),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('left to right labeling',original_image)
    cv2.waitKey()
    x,y,w,h = cv2.boundingRect(c)
    
    #cropping image
    cropped_contour = original_image[y:y+h,x:x+w]
    image_name = 'output image_' + str(i+1) + '.jpg'
    print(image_name)
    cv2.imwrite(image_name,cropped_contour)
    
    
    
    
    
    
    
        
    
    





cv2.destroyAllWindows()

