import cv2
import numpy as np

img = cv2.imread(r"c:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\minecraft.png")
#cv2.imshow("Minecraft", img)

img2 = cv2.rectangle(img, (100,100), (200,200), (0,255,0), 5)
#cv2.imshow("rectangle",img2)

img3 = cv2.circle(img, (300,300), 50, (0,0,255), -1)
#cv2.imshow("circle", img3)

img4 = cv2.putText(img, "Furkan", (100,400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 5)
cv2.imshow("text", img4)


cv2.waitKey(0)
cv2.destroyAllWindows()