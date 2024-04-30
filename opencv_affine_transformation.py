import cv2
import numpy as np 

img = cv2.imread("Ferrari16.jpg")

cv2.namedWindow("img",cv2.WINDOW_NORMAL )

print(img.shape)


rows,cols = img.shape[:2]

src_point = np.float32([[0,0],[cols-1,0],[0,rows-1]])
dst_point = np.float32([[0,0],[int((cols-1)*0.6),0],[int((cols-1)*0.4),rows-1]])

affine_matrix = cv2.getAffineTransform(src_point, dst_point)

img_output = cv2.warpAffine(img, affine_matrix, (cols,rows))


cv2.imshow("img",img)
cv2.imshow("img_output",img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()