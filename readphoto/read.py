import cv2 as cv

img = cv.imread('steam.jpg')


def rescaleframe(frame,scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


resize = rescaleframe(img)
cv.imshow('steam',img)
cv.imshow('steam_resize',resize)
cv.waitKey(0)