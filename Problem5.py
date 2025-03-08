#5. Geometrik Şekiller Çizme
#Boş bir görüntü oluştur (örneğin, siyah bir arka plan) ve üzerine, Çizgi, Dikdörtgen, Daire, Metin ekle.
import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.line(image, (50, 50), (450, 50), (255, 0, 0), 3)
cv2.rectangle(image, (50, 100), (450, 200), (0, 255, 0), 3)
cv2.circle(image, (250, 350), 50, (0, 0, 255), 3)
cv2.putText(image, "OpenCV", (150, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Geometrik Sekiller", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
