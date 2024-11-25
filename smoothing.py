import cv2 as cv
img=cv.resize((cv.imread('photos/park.jpg')),(500,500),interpolation=cv.INTER_AREA)
cv.imshow("park",img)

# Averaging
average = cv.blur(img, (3,3)) #(3,3) is kernel size
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0) # 0 is the sigma x (standard deviation of x)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)  # 3 is the kernel size
cv.imshow('Median Blur', median)

# Bilateral [mostly used- apply blur but retains the edges]
bilateral = cv.bilateralFilter(img, 10, 35, 25)  # 10= diameter of kernel, 35= sigma color(larger no. means  more colors in neighbours), 25=sigmaspace(larger no. means more neighbour colors influence the current color)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)