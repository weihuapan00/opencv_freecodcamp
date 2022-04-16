import cv2 as cv

img = cv.imread('steam.jpg')
def rescaleframe(frame,scale = 0.5):

cv.imshow('steam',img)
cv.waitKey(0)