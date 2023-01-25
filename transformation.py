import cv2 as cv
import numpy as np
img =cv.imread('picture/cat1.jpg')
#cv.imshow('CAT1',img)
resized =cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
# #translation
# def translate(resized,x,y):
#     transMat= np.float32([[1,0,x],[0,1,y]])
#     dimensions = (resized.shape[1], resized.shape[0])
#     return cv.warpAffine(resized,transMat, dimensions)
# #-x --> left
# #-y --> up
# #x--> right
# #y -->down
# translated= translate(resized,100,100)
# cv.imshow('Translated',translated)
# #rotation
# def rotate(img,angle,rotPoint=None):
#     (height,width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint =(width//2,height//2)
#     rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions = (width,height)
#     return cv.warpAffine( resized, rotMat, dimensions)
# rotated = rotate(resized,45)
# cv.imshow('rotate',rotated)
# rotated_2= rotate(rotated,-45)
# cv.imshow('Rotated2',rotated_2)


#fliping
flip =cv.flip(resized,1)
cv.imshow('Flip',flip)

cv.waitKey()