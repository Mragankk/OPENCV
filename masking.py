import cv2 as cv
import numpy as np

img = cv.resize((cv.imread('photos/jasii.jpg')),(500,500),interpolation=cv.INTER_AREA)

blank_img=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("BLANK",blank_img)

mask=cv.circle(blank_img,(img.shape[1]//2 ,img.shape[0]//2 -60),100,255,thickness=-1)
cv.imshow("masked",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("MASKED",masked)

cv.waitKey(0)