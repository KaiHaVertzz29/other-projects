import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')

blank[:]=0,255,255

cv.imshow('blank',blank)


cv.waitKey(0)

video=cv.VideoCapture(0)


while True:

    isTrue,frame=video.read()

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    blurr=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

    border=cv.Canny(blurr,40,50)

    #ret,thresold=cv.threshold(gray,80,100,cv.THRESH_BINARY)

    cv.imshow('img',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()

