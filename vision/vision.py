import cv2
import numpy as np


cap = cv2.VideoCapture(2)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking

h,s,v = 180,255,255
# Creating track bar
cv2.createTrackbar('h', 'result', 0, 179, nothing)
cv2.createTrackbar('s', 'result', 0, 255, nothing)
cv2.createTrackbar('v', 'result', 0, 255, nothing)

cv2.createTrackbar('h2', 'result', 0, 179, nothing)
cv2.createTrackbar('s2', 'result', 0, 255, nothing)
cv2.createTrackbar('v2', 'result', 0, 255, nothing)


while(True):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('h', 'result')
    s = cv2.getTrackbarPos('s', 'result')
    v = cv2.getTrackbarPos('v', 'result')

    h2 = cv2.getTrackbarPos('h2', 'result')
    s2 = cv2.getTrackbarPos('s2', 'result')
    v2 = cv2.getTrackbarPos('v2', 'result')

    lower_val = np.array([h, s, v])
    upper_val = np.array([h2, s2, v2])

    mask = cv2.inRange(hsv, lower_val, upper_val)
    

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print("Min HSV:", h, s, v)
        print("Max HSV:", h2, s2, v2)
        break

cap.release()

cv2.destroyAllWindows()