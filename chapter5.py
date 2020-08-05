#Warp Perspective
import cv2
import numpy as np

img = cv2.imread('pic2.png')

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('image', img)
cv2.imshow('Output',imgOutput)
# cv2.waitKey(0)

#Joining Images

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow('Image Horizontal',imgHor)
cv2.imshow('Image Vertical',imgVer)


cv2.waitKey(0)