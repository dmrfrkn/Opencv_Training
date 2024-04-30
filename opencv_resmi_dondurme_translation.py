import cv2
import numpy as np
img = cv2.imread("Ferrari16.jpg")

cv2.namedWindow("img",cv2.WINDOW_NORMAL )

print(img.shape)


rows,cols = img.shape[:2]

# =============================================================================
#  RESMIN KONUMUYLA OYNAMA
#rows,cols = img.shape[:2]    
# 
# translation_matrix = np.float32([[1,0,500],[0,1,25]])
# 
# 
# img_translation = cv2.warpAffine(img, translation_matrix, (cols,rows))
# 
# =============================================================================
# =============================================================================
# RESMI YENIDEN BOYUTLANDIRMA
# res = cv2.resize(img, (300,300))
# # res = cv2.resize(img,None,fx=0.4,fy=1,interpolation = cv2.INTER_CUBIC)
# =============================================================================

# =============================================================================
# ##RESMI DONDURME
# 
# rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),-30, 1)
# 
# img_rotation = cv2.warpAffine(img, rotation_matrix, (cols,rows))
# =============================================================================





cv2.imshow("img",img)
cv2.imshow("img_rotation",img_rotation)

cv2.waitKey(0)
cv2.destroyAllWindows()






















