##1. Görüntüyü Yükleme ve Gösterme
##Bir görüntüyü OpenCV ile yükle ve ekranda göster.Kullanıcı bir tuşa bastığında görüntüyü kapat.
import cv2
img_path = r"C:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\JR\minecraft.png"
img = cv2.imread(img_path,1)

cv2.imshow("Görüntü",img)

cv2.waitKey(0)
cv2.destroyAllWindows()