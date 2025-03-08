import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.imshow("Black", img) 

img2 = cv2.line(img, (0,0), (511,511), (255,0,0), 5)

cv2.imshow("Blue Line", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()