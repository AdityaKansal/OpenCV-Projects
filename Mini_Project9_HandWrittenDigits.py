# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:02:48 2018

@author: akansal2
"""


#importing librairies
import cv2
import numpy as np
import dlib





#path
path = 'C:/A_stuff/Learning/Machine Learning/Udemy/Computer Vision OpenCV/Rajiv Material/Master OpenCV/'



#lets open the training image
image = cv2.imread(path + 'images/digits.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
small = cv2.pyrDown(image)

cv2.imshow('Image',small)
cv2.waitKey()
cv2.destroyAllWindows()

print(gray.shape)  #1000*2000

#to get 20*20 pixel
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

x = np.array(cells)
print(str(x.shape))


#spliting this data in train and test set
train = x[:,:70].reshape(-1,400).astype(np.float32)
test = x[:,70:100].reshape(-1,400).astype(np.float32)


#creating labels fo train and test set
k = [0,1,2,3,4,5,6,7,8,9]
train_labels = np.repeat(k,350)[:,np.newaxis]
test_labels = np.repeat(k,150)[:,np.newaxis]


#Initiate KNN
knn = cv2.ml.KNearest_create()
knn.train(train,train_labels)
ret,result,neighbours,distance = knn.find_nearest(test,k=3)


#accuracy
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct*(100.0/result.size)

print(accuracy)

































