import cv2 as cv
#reading image
#img =cv.imread('Picture/cat2.jpg')
#cv.imshow('cat1',img)
capture =cv.VideoCapture('Videos/Pexels Videos 1526909.MP4')
while True:
    isTrue ,frame =capture.read()
    cv.imshow('Pexels Videos 1526909',frame)
    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
    capture.release()
    cv.destroyAllWindows()
