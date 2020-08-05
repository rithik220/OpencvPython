#Resizing and Cropping
import cv2
import numpy as np

img = cv2.imread('lena.jpg')
print(img.shape)
imgResize = cv2.resize(img,(300,350))
print(imgResize.shape)
imgCropped = img[0:300,0:200]

cv2.imshow('image', img)
cv2.imshow('image Resize', imgResize)
cv2.imshow('image cropped', imgCropped)
cv2.waitKey(0)

