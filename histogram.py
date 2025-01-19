import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.resize((cv.imread('photos/PF.jpg')),(500,500),interpolation=cv.INTER_AREA)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


blank=np.zeros((gray.shape[:2]),dtype='uint8')
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("MASK CIRCLE",circle)

masked=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow("MASK",masked)


''' GRAYSCALE histogram'''
# passing images as list
gray_hist=cv.calcHist([gray],[0],masked,[256],[0,256])
plt.figure()
plt.title("GRAYSCALE HISTOGRAM")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


''' COLOR HISTOGRAM'''
colors=('b','g','r')
for i, col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
    plt.title('COLOR HISTOGRAM')
plt.show()

cv.waitKey(0)