import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(x):
    pass

cv2.namedWindow("track")
cv2.createTrackbar("Hue min: ","track",0,179,empty)
cv2.createTrackbar("Hue max: ","track",179,179,empty)
cv2.createTrackbar("Sat min: ","track",0,255,empty)
cv2.createTrackbar("Sat max: ","track",255,255,empty)
cv2.createTrackbar("Val min: ","track",0,255,empty)
cv2.createTrackbar("Val max: ","track",255,255,empty)


while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(720,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min: ","track")
    h_max = cv2.getTrackbarPos("Hue max: ","track")
    s_min = cv2.getTrackbarPos("Sat min: ","track")
    s_max = cv2.getTrackbarPos("Sat max: ","track")
    v_min = cv2.getTrackbarPos("Val min: ","track")
    v_max = cv2.getTrackbarPos("Val max: ","track")

    l_hsv = np.array([h_min,s_min,v_min])
    h_hsv = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(hsv,l_hsv,h_hsv)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(h_max,h_min,s_max,s_min,v_max,v_min)
cv2.destroyAllWindows()
cap.release()