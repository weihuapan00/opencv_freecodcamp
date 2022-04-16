import cv2 as cv

video = cv.VideoCapture('video.mp4')

def rescaleframe(frame,scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = video.read()
    frame_resize = rescaleframe(frame)
    cv.imshow('video_resize',frame_resize)
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()