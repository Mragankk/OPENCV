import cv2 as cv


''' Reading Images'''
img=cv.imread('photos/jasii.jpg') # takes path to image and returns the image as matrix of pixels!
cv.imshow('jasii',img) # to show the image in new window( takes 2 args picture title and picture to be displayed)
cv.waitKey(10)  # wait until pressing any key to continue 

'''Reading Videos'''
vid=cv.VideoCapture('videos\dog_running.mp4')  # vid is the instance of the videoCapture clause

while True:  # using while loop to process the video
    isTrue, frame = vid.read() # video is provided frame by frame [.read() returns two values- True or False(when vid ends)] [frame is in the form of numpy array ]
    cv.imshow("VIDEO",frame)   # to display the image in new window named "VIDEO"
    
    if cv.waitKey(20)&0xff==ord('d'):  # someway to stop the while loop [0xff==ord('d')] means when d is pressed break the loop and stop the dsplay of the video
        break
vid.release() # releases or frees the video file or camera resource
cv.destroyAllWindows() # stop all the openCV-created window