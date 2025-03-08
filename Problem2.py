import cv2
img_path = r"C:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\JR\minecraft.png"
img = cv2.imread(img_path,1)

##2. Görüntüyü Gri Tonlamaya Çevir
##Bir renkli görüntüyü gri tonlamaya çevir ve hem renkli hem de gri tonlama görüntüyü yan yana göster.
image = cv2.imread(img_path,0)

cv2.imshow("Görüntü",img)
cv2.imshow("Gri Tonlama",image)

cv2.waitKey(0)
cv2.destroyAllWindows()