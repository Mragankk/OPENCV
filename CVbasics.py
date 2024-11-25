import cv2 as cv

img=cv.imread('photos/jasii.jpg') #BGR image
# cv.imshow("jasii", img)
# cv.waitKey(0)

# converting grayscale(B&W image)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converting img[jasii.jpg] to (GRAYSCALE)B&W image
# cv.imshow("GRAY",gray)
# cv.waitKey(0)

temple=cv.imread('photos/LOTUS_TEMPLE.jpg')
temple=cv.resize(temple,(1000,750))
gray_temple=cv.cvtColor(temple,cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY TEMPLE',gray_temple)
# cv.waitKey(0)

# BLUR image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('BLUR',blur)
# cv.waitKey(0)

# Edge cascade
# cany=cv.Canny(temple,125,175)
# cv.imshow("cany",cany)
# cv.waitKey(0)

cany2=cv.Canny(blur,125,175)
# cv.imshow("cany blur",cany2)
# cv.waitKey(0)


# Dilating the image
dilated=cv.dilate(cany2,(3,3),iterations=1)
# cv.imshow("dilated",dilated)
# cv.waitKey(0)

# ERODING [opposite of dilating]
eroded=cv.erode(dilated,(3,3),iterations=1)
# cv.imshow("ERDOED",eroded)
# cv.waitKey(0)

# RESIZE 
resized=cv.resize(img,(500,400),interpolation=cv.INTER_CUBIC)
# cv.imshow('resized',resized)
# cv.waitKey(0)

# CROPPING
croped=img[100:350, 350:800]
# cv.imshow("CROPPED",croped)
# cv.waitKey(0)