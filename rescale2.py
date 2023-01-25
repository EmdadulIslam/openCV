import cv2 as cv
img =cv.imread('Picture/cat2.jpg')
def rescaleFrame(frame,scale=0.25):
     #image video live video
    width =int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
def changeRes(width,height)
   #live video
    cpature.set(3,width)
    capture.set(4,height)
capture =cv.VideoCapture('Videos/Pexels Videos 1526909.MP4')
while True:
    isTrue ,frame =capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Pexels Videos 1526909',frame)
    cv.imshow('Pexels Videos 1526909 resized',frame_resized)
    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
capture.release()
cv.destroyAllWindows()