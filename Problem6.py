#Canlı Görüntüde Aynalama
#Web kamerasından gelen görüntüyü yatay olarak aynala (mirror efekti) ve ekranda göster.

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    mirrored_frame = cv2.flip(frame, 1)
    cv2.imshow("Orijinal", frame)
    cv2.imshow("Aynalanmis Goruntu", mirrored_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()

