#9. Basit Çizim Aracı
#Fare ile tıklayarak bir pencere üzerinde basit şekiller (örneğin, daire veya dikdörtgen) çizebileceğin bir uygulama yap.
import cv2
import numpy as np
#BU BİRAZ KARMAŞIK GÖRÜNÜYOR PAS GEÇİLEBİLİR

# Çizim durumu için global değişkenler
drawing = False  # Çizim yapılıyor mu?
start_point = None  # Dikdörtgen için başlangıç noktası
mode = 'rectangle'  # Çizim modu: 'rectangle' veya 'circle'

# Fare olayları için geri çağırma fonksiyonu
def draw_shape(event, x, y, flags, param):
    global drawing, start_point, mode, image

    if event == cv2.EVENT_LBUTTONDOWN:  # Sol tuşa basıldığında
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:  # Fare hareket ederken
        if drawing:
            temp_image = image.copy()
            if mode == 'rectangle':
                cv2.rectangle(temp_image, start_point, (x, y), (255, 0, 0), 2)
            elif mode == 'circle':
                radius = int(((x - start_point[0]) ** 2 + (y - start_point[1]) ** 2) ** 0.5)
                cv2.circle(temp_image, start_point, radius, (0, 255, 0), 2)
            cv2.imshow('Drawing App', temp_image)

    elif event == cv2.EVENT_LBUTTONUP:  # Sol tuş bırakıldığında
        drawing = False
        if mode == 'rectangle':
            cv2.rectangle(image, start_point, (x, y), (255, 0, 0), 2)
        elif mode == 'circle':
            radius = int(((x - start_point[0]) ** 2 + (y - start_point[1]) ** 2) ** 0.5)
            cv2.circle(image, start_point, radius, (0, 255, 0), 2)
        cv2.imshow('Drawing App', image)

# Boş bir görüntü oluştur
image = np.ones((600, 800, 3), dtype=np.uint8) * 255

# Pencereyi oluştur ve fare olaylarını ayarla
cv2.namedWindow('Drawing App')
cv2.setMouseCallback('Drawing App', draw_shape)

print("Modları değiştirmek için 'r' (dikdörtgen) veya 'c' (daire) tuşuna basın. Çıkmak için 'q' tuşuna basın.")

while True:
    cv2.imshow('Drawing App', image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):  # Dikdörtgen moduna geç
        mode = 'rectangle'
    elif key == ord('c'):  # Daire moduna geç
        mode = 'circle'
    elif key == ord('q'):  # Çıkış
        break

cv2.destroyAllWindows()
