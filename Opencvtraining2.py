import cv2
import numpy as np7
import matplotlib.pyplot as plt

image = cv2.imread(r"c:\Users\CumFur\Desktop\Furkan\VS Code\ImageProcessing\minecraft.png")
plt.imshow(image,cmap= "gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([])
plt.show()
