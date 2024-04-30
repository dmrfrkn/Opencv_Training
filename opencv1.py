import cv2 
from matplotlib import pyplot as plt
resim = cv2.imread("Ferrari.jpg",100)
  
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)


cv2.imshow("resim",resim)


                 
cv2.imshow("resim penceresi",resim)
plt.imshow(resim)
plt.show()


k = cv2.waitKey(0)
cv2.destroyWindow("resim penceresi")
#cv2.destroyAllWindows()
#print(k)

if k == 27:
    print("ESC tuşuna basıldı ve uygulamadan çıkış yapıldı")
elif k == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi")
cv2.imwrite("Ferrari16.jpg", resim)


