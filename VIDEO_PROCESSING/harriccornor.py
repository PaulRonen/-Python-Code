import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True :
    ret, frame = cap.read()
    if not ret:
       break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    dst = cv.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[127,0,32]

    cv.imshow('dst',frame)
    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()