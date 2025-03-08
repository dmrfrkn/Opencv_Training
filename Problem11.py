#11. Görüntüyü Döndürme
#Bir görüntüyü belirli bir derece (örneğin, 90° veya 45°) döndür ve sonucu göster.
import cv2
import numpy as np

img_path = r"C:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\JR\minecraft.png"
image = cv2.imread(img_path)

angle = 45  

(h, w) = image.shape[:2]

center = (w // 2, h // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

cv2.imshow("Original Image", image)
cv2.imshow(f"Rotated Image ({angle} degrees)", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

