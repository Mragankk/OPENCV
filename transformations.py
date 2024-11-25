import cv2 as cv
import numpy as np

img=cv.imread('photos/jasii.jpg')

'''TRANSLATION [shifting image along x nad y axis i.e move up down left right]'''
def translate(img,x,y):
    transMAT=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMAT,dimensions)

# -x > left
# -y > Up
# x  > Right
# y  > Down 

translated=translate(img,-100,-100)  # try -100,100 or -100,-100
# cv.imshow("TRANSLATED IMAGE",translated)
# cv.waitKey(0)

'''ROTATING'''
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated_img=rotate(img,180) # for clockwise -45
# cv.imshow("IMAGE ROTATED",rotated_img)
# cv.waitKey(0)

'''RESIZING'''
resized_img=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow("RESIZED IMAGE",resized_img)
# cv.waitKey(0)

'''FLIPPING'''
flip=cv.flip(img,1) # code could be 0(verticle),1(horizontal),-1(flipping both vertically and horizontally)
# cv.imshow("flipped",flip)
# cv.waitKey(0)

'''CROPPING'''
cropped=img[100:500,350:800]
# cv.imshow("CROPPED",cropped)
# cv.waitKey(0)