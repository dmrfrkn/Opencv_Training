#10. Piksel Değerlerine Erişim
#Bir görüntünün belirli bir pikselinin rengini yazdır.
#Örneğin, kullanıcıdan bir pikselin koordinatlarını al ve oradaki RGB veya gri tonlama değerini göster.
import cv2

# Fare geri çağırma fonksiyonu
def get_pixel_value(event, x, y, flags, param):
    global image
    if event == cv2.EVENT_LBUTTONDOWN:  # Sol fare tuşuna basıldığında
        if len(image.shape) == 3:  # Renkli görüntü (BGR)
            b, g, r = image[y, x]
            print(f"Koordinatlar ({x}, {y}): B={b}, G={g}, R={r}")
        else:  # Gri tonlama görüntü
            gray_value = image[y, x]
            print(f"Koordinatlar ({x}, {y}): Gri Tonlama Değeri={gray_value}")

# Görüntüyü yükleme
image_path = r'C:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\JR\minecraft.png'  # Görüntü dosyasının yolu
image = cv2.imread(image_path)

if image is None:
    print("Görüntü yüklenemedi. Lütfen geçerli bir dosya yolu girin.")
else:
    # Pencere oluştur ve fare geri çağırma ayarla
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', get_pixel_value)

    # Görüntüyü göster
    print("Bir piksele tıklayarak renk değerlerini görebilirsiniz. Çıkmak için bir tuşa basın.")
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
