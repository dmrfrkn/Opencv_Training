import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.rectangle(frame, (100, 100), (200, 200), (0, 255, 0), 3)
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord ("q"):
        break

    


cap.release()
cv2.destroyAllWindows()    