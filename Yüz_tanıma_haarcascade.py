import cv2

# Önceden eğitilmiş Haar Cascade yüz tanıma modelini yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()
    
    # Görüntüyü gri tona dönüştür (yüz tanıma için daha iyi)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Algılanan yüzleri çerçeve içine al
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Sonuçları göster
    cv2.imshow('Yüz Algılama', frame)
    
    # Çıkış için 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
cap.release()
cv2.destroyAllWindows()
