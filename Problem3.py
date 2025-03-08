#3. Video Kaynağını Göster
#Web kamerasından gelen görüntüyü al ve gerçek zamanlı olarak ekranda göster.
#Kullanıcı bir tuşa bastığında görüntüyü durdur.
import cv2

cap = cv2.VİdeoCapture(0)   
while True:
    ret, frame = cap.read()
    cv2.imshow("Kamera",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()
