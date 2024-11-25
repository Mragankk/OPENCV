'''Contours in OpenCV are curves that join all continuous points
along a boundary with the same intensity.
They are often used in image processing and computer vision to detect 
and analyze the shapes, sizes, and features of objects in an image'''


import cv2 as cv
import numpy as np

img=cv.imread('photos/PF.jpg')
img=cv.resize(img,(600,600),interpolation=cv.INTER_CUBIC)
# cv.imshow('image',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray)
# canny=cv.Canny(img,125,175)
# cv.imshow("canny edges",canny)



'''THRESHHOLDING [Converting image into binary format-0[black] or 1[white]]'''
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow("threshold",thresh)
# cv.waitKey(0)

contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)


blank=np.zeros(img.shape,dtype='uint8')
# cv.imshow("blank",blank)

cv.drawContours(blank,contours,-1,(0,255,125),1)
# cv.imshow("contours drawn",blank)
# cv.waitKey(0)