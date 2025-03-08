#7. Renk Ayıklama
#Kullanıcının seçtiği bir rengi (örneğin, kırmızı) görüntüden filtrele ve sadece o rengi göster.
import cv2
import numpy as np

img_path = r"C:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\JR\minecraft.png"
image = cv2.imread(img_path,1)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])  # Kırmızı için alt sınır
upper_red = np.array([10, 255, 255])  # Kırmızı için üst sınır
lower_red2 = np.array([170, 120, 70])  # Kırmızı için ikinci aralık
upper_red2 = np.array([180, 255, 255])  # Kırmızı için ikinci üst sınır

mask1 = cv2.inRange(hsv_image, lower_red, upper_red)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
mask = cv2.add(mask1, mask2)

filtered_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
