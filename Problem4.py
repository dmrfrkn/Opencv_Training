#4. Görüntüyü Kaydet
#   Bir görüntüyü yükle, üzerine bir işlem (örneğin, gri tonlama) uygula ve sonucu bir dosyaya kaydet.

import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü yok!")
        break
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Kamera - Orijinal", frame)
    cv2.imshow("Kamera - Gri Tonlama", gray_frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):  
        cv2.imwrite("kaydedilen_goruntu.jpg", gray_frame)
        print("Görüntü kaydedildi.")
    elif key == ord("q"):  
        break

cap.release()
cv2.destroyAllWindows()
