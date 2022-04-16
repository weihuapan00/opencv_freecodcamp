import cv2 as cv

img = cv.imread('steam.jpg')


def rescaleframe(frame,scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('steam',img)
img_resize = rescaleframe(img,scale=0.1)

cv.imshow('steam_resize',img_resize)
cv.waitKey(0)