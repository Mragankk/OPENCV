'''Rescaling- it means to change the width and height of image or video
It is a good practice to down scale or change the height and weight of the video than the original 
because many web cams dont support going higher than their max limit'''


import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    # it will work for Images, Videos ad Live videos
    width = int(frame.shape[1]*scale) # frame.shape=[width,height]
    height= int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
#     only works for live videos(web cams)
    livVid.set(3,width)
    livVid.set(4,height)


'''VIDEO RESCALING'''
vid=cv.VideoCapture('videos\dog_running.mp4')  
while True:
    isTrue, frame = vid.read()

    frame_resized=rescaleFrame(frame,scale=.5)
    cv.imshow("VIDEO",frame)
    cv.imshow("VIDEO RESCALED",frame_resized)
    
    if cv.waitKey(20)&0xff==ord('0'):
        break
vid.release()
cv.destroyAllWindows()


'''IMAGE RESCALING'''
img=cv.imread('photos\jasii.jpg')
resized_image=rescaleFrame(img)

cv.imshow("RESIZED PICTURE",resized_image)
cv.waitKey(0)



'''Live video capture'''
livVid=cv.VideoCapture(0)

if not livVid.isOpened():
    print("Error: Could not open webcam.")
    exit()

changeRes(246,680)  # Set resolution to 640x480 could be - 1280x720 or 1920x1080

while True:
    istrue, frame = livVid.read()
    if not istrue:
        print("Error")
        break
    cv.imshow('Live Webcam', frame)
    if cv.waitKey(20) & 0xFF==ord('x'):
        break
livVid.release()
cv.destroyAllWindows()

