import cv2 
import numpy as np

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter("FurkanDMR.avi",fourcc,30.0,(640,480))

def nothing(x):
    pass
cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame",0,359,nothing)
cv2.createTrackbar("H2","frame",0,359,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,255,nothing)
cv2.createTrackbar("V2","frame",0,255,nothing)

if not cam.isOpened():
    print("Kamera tanınmadı")
    
while True:
    ret, frame = cam.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    H1 = int(cv2.getTrackbarPos("H1", "frame") /2)
    H2 = int(cv2.getTrackbarPos("H2", "frame") /2)
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")
    
    lower = np.array([H1,S1,V1])
    upper = np.array([H2,S2,V2])
    
                
    # lower = np.array([0, 90, 160])   #Red in HSV
    # upper = np.array([10, 200, 255]) #Red in HSV
    
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask = mask)
    
    contours, ret = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 100:  
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255 ,0), 2) 
    

    out.write(frame)
    cv2.imshow("frame", frame)
    cv2.imshow("pencere1", mask)
    cv2.imshow("pencere2", res)
    #cv2.imshow("pencere3", rectangle_img)
    if cv2.waitKey(1) == ord("q"):
        print("Uygulama sonlandırıldı")
        break

cam.release()
out.release()
cv2.destroyAllWindows()
