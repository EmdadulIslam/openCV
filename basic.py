import cv2 as cv
img =cv.imread('picture/cat1.jpg')
#cv.imshow('Cat2',img)
#resize image method 1
# def rescaleFrame(frame,scale=0.25):
#     width =int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
#     dimensions = (width,height)
#     return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
# resized_image = rescaleFrame(img)
#cv.imshow('Image',resized_image)

#converting to grayscale
#gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)
# #Blur
# blur =cv.GaussianBlur(resized_image,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
# #Edge casecade
# canny =cv.Canny(resized_image,125,175)
# cv.imshow('canny edges',canny)
# resize method 2
resized =cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropped 
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)


