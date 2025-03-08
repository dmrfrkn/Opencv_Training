#8. Görüntüyü Yeniden Boyutlandırma
#Bir görüntüyü farklı boyutlara ölçeklendir (örneğin, %50 küçültme, %200 büyütme).
#Görüntüyü bir pencere içinde göster.
#PAS GEÇİLEBİLİR
import cv2

img_path = r"C:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\JR\minecraft.png"
image = cv2.imread(img_path,1)

original_height, original_width = image.shape[:2]

# %50 küçültme için ölçek faktörü
scale_down = 0.5
new_width = int(original_width * scale_down)
new_height = int(original_height * scale_down)
resized_down = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

# %200 büyütme için ölçek faktörü
scale_up = 2.0
new_width = int(original_width * scale_up)
new_height = int(original_height * scale_up)
resized_up = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original Image', image)
cv2.imshow('Resized Down (50%)', resized_down)
cv2.imshow('Resized Up (200%)', resized_up)

cv2.waitKey(0)
cv2.destroyAllWindows()
