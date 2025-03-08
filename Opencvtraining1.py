import cv2
import numpy as np

image_path = r"c:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\minecraft.png"
image = cv2.imread(image_path, 1)

cv2.imshow("Minecraft", image)
##cv2.imwrite("MC gri foto.png", image) ##Burada png jpg jpeg olarak kaydedebiliriz 

q = cv2.waitKey(0)
if q == 27:
    cv2.destroyAllWindows()
elif q == ord("s"):
    cv2.imwrite("m ri .jpg", image)