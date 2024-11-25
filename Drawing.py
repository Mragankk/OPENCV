import cv2 as cv
import numpy as np


'''displaying existing photo'''
# img=cv.imread("photos/jasii.jpg")
# cv.imshow("JASII", img)
# cv.waitKey(0)


'''Creating own blank photo using numpy'''
blank=np.zeros((500,500,3), dtype='uint8')   # blank is a image created using numpy arrays of height and width 500,500, dtype 'uint8' means image, 3 indicates no. of color channels(ex-BGR)
# cv.imshow("BLANK IMAGE", blank)

# coloring an image
# blank[:]=0,255,0    # color whole blank as green (B G R)
# cv.imshow("GREEN IMAGE", blank)
# cv.waitKey(0)

'''drawing shapes in image and writing text'''
# SQUARE
# blank[200:300, 300:400]=0,0,255
# cv.imshow("DRAW SHAPE", blank)
# cv.waitKey(0)

# RECTANGLE
# cv.rectangle(blank,(100,150),(300,350),(0,0,255),thickness=5) # Hollow rectangle
# cv.imshow(" HOLLOW RECTANGLE", blank)
# cv.waitKey(0)

# cv.rectangle(blank,(100,150),(300,350),(0,0,255),thickness=cv.FILLED)
# cv.imshow("RECTANGLE", blank)
# cv.waitKey(0)


# CIRCLE
# cv.circle(blank,(250,250),50,(0,0,255),thickness=5)
# cv.circle(blank,(250,250),80,(0,255,255),thickness=5)
# cv.imshow("circle",blank)
# cv.waitKey(0)

# LINE
# cv.line(blank,(250,250),(500,500),(255,255,255),thickness=2)
# cv.imshow("LINE",blank)
# cv.waitKey(0)

# WRITE TEXT
cv.putText(blank,"HELLO WORLD!",(180,225),cv.FONT_HERSHEY_COMPLEX,1.0,255,2)
cv.imshow("TEXT",blank)
cv.waitKey(0)