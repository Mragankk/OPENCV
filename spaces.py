'''color spaces are systems that represent colors in various formats, such as RGB, HSV, LAB, and more.
OpenCV provides extensive support for converting between different color spaces, 
which is essential for tasks like object detection, image enhancement, or segmentation.'''

import cv2 as cv
img=cv.imread('photos/park.jpg')
img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("original",img)

# BGR to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


# BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)


# BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)


# BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

'''Till now we have seen that we can convert BGR to all other but we cannot do vice versa
to do so we first have to convert to BGR then to any other'''

lab_Bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab-->bgr',lab_Bgr)
cv.waitKey(0)