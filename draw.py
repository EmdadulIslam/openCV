import cv2 as cv 
import numpy as np
blank =np.zeros((500,500,3),dtype ='uint8')
#cv.imshow('Blank',blank)
# #1. paint image
# blank[:]=0,255,0
# cv.imshow('Green',blank)
#2. draw rectangle
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2 )
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED )# FILLED=-1
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)
# # 3.draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)
# #4. draw a line 
# cv.line(blank,(100,250),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.imshow('Line',blank)
# 5. write a text on image
cv.putText(blank,'Hello',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)