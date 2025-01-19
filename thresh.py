'''Thresholding is a technique in image processing used to convert grayscale images into binary images.
It applies a threshold value to pixel intensities, separating them into two categories, typically 
representing foreground and background.'''

'''In thresholding we set a threshold value and compare it with other picxels
If compared pixel has value less than threshold value , set that pixel intensity to 0(black) else 255(white)'''
import cv2 as cv

img=cv.resize((cv.imread('photos/park.jpg')),(500,500),interpolation=cv.INTER_AREA)
cv.imshow("pic",img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)


# 1.SIMPLE THRESHOLD
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY) # Threshold= value passed(here 150), thesh=image converted to binary, passing parametres-> image(gray), threshold value(150), if pixel>threshold change intensity to value(here 255),cv.THRESH_BINARY(converting to binary)
cv.imshow("SIMPLE THRESHOLD",thresh)

# inverting thresholding
threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) # Threshold= value passed(here 150), thesh=image converted to binary, passing parametres-> image(gray), threshold value(150), if pixel>threshold change intensity to value(here 255),cv.THRESH_BINARY(converting to binary)
cv.imshow("SIMPLE THRESHOLD INVERTED",thresh_inv)


#2. ADAPTIVE THRESHOLDING
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("ADAPTIVE THRESHOLD",adaptive_thresh)
cv.waitKey(0)

