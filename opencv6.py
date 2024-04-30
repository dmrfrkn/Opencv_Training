import cv2
import matplotlib.pyplot as plt
resim = cv2.imread("Ferrari16.jpg")

kirp = resim[100:500,100:500]
# resim[0:300,0:200] = kirp

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(kirp)
plt.show()