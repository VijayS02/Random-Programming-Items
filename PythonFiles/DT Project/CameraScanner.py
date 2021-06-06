import numpy as np
import cv2

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

cap = cv2.VideoCapture(0)

t_minus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    dimg=diffImg(t_minus, t, t_plus)
    threshold = 200000
    if cv2.countNonZero(dimg) > threshold:
        cv2.putText(frame, "Room Status: {}".format('movement'), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Room Status: {}".format('no movement'), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('Movement indicator',frame)

    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)



    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow('Movement indicator')
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

