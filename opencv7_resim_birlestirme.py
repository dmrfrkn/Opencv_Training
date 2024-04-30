# import cv2
# import numpy as np

# =============================================================================
# # x = np.uint8([250])
# # y = np.uint8([10])
# # sonuc1 = x+y
# # sonuc2 = cv2.add(x,y)
# 
# =============================================================================

# 2 RESMI BIRLESSTIRME
# =============================================================================
# img1 = cv2.imread("qwe.png")
# img2 = cv2.imread("asd.png")
# toplam = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# =============================================================================

####
####
##BITSEL ISLEMLER
import cv2
import numpy as np

img1 = cv2.imread("Ferrari16.jpg")
img2 = cv2.imread("qwe.png")

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)

x,y,z = img1.shape
roi = img2[0:x,0:y]




img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1_gray, 10, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img1,img1,mask = mask)

toplam = cv2.add(img1_bg,img2_fg)

img2[0:x,0:y] = toplam


cv2.imshow("resim",img2)
# cv2.imshow("resim2",img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()






























    