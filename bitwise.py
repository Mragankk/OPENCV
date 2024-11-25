import numpy as np
import cv2 as cv

img= cv.imread('photos/park.jpg')

blank=np.zeros((500,500),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(470,470),255,-1)
circle=cv.circle(blank.copy(),(250,250),240,255,-1)

cv.imshow("rectangle",rectangle)
cv.imshow('circle',circle)

# Bitwise AND [intersecting regions]
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("rectangle and Circle",bitwise_and)

# Bitwise OR [non-intersecting and intersecting regions]
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("rectangle or circle",bitwise_or)
 
# Bitwise XOR [Intersecting regions]
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Rectangle xor circle',bitwise_xor)

# Bitwise NOT 
bitwise_not=cv.bitwise_not(circle)
cv.imshow("circle NOT",bitwise_not)
cv.waitKey(0)