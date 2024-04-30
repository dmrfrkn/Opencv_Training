import cv2

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")# video sıkıstırma formatı

out = cv2.VideoWriter("alisamiyen.avi",fourcc,30.0,(640,480))
        
while cam.isOpened():   
    ret, frame = cam.read()
    
    if not ret:
        print("kamera okunmadı")
        break


    out.write(frame)
    
    cv2.imshow("kamera",frame)
    if cv2.waitKey(1) == ord("q"):
        print("video bitti")
        break


cam.release()
out.release()
cv2.destroyAllWindows()