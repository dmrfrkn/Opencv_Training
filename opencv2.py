# =============================================================================
# import cv2
# 
# 
# import numpy as np
# 
# sifir = np.zeros([300,300])
# 
# bir = np.ones([300,300])
# 
# cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
# cv2.namedWindow("bir",cv2.WINDOW_NORMAL)
# cv2.imshow("sifir", sifir)
# cv2.imshow("bir",bir)
# cv2.waitKey(0)
# 
# cv2.destroyAllWindows() 
# =============================================================================
# =============================================================================
# 
# import cv2
# 
# cam =cv2.VideoCapture(0)  #kamerayı tanımladık ve algılattık  
# 
# 
# cam.set(3,320) # kameranın boyutlarını ayarladık
# cam.set(4,240)   
# if not cam.isOpened():#kameranın algılanıp algılanmadığını komtrol ettik
#     print("kamera tanınmadı")
#     exit()
# while True:
#     ret, frame = cam.read() # ret true ya da false deger döndürür 
#    #kameradan goruntunun okunup okkunamadıgına dair bize bilgi verir
#     #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#        
#     if not ret:
#         print("Kameradan görüntü okunamıyor")   
#         break        
#     cv2.imshow("kamera",frame)
# 
#     if cv2.waitKey(1)& 0xFF == ord("q"):
#         print("görüntü sonlandırıldı")
#         break
# 
# cam.release()#kameranın kapanması için bu kodu yazdık
# cv2.destroyAllWindows() 
# =============================================================================
# =============================================================================
# import cv2
# cam = cv2.VideoCapture("AliSamiYen.mp4",)
# 
# while cam.isOpened():
#     ret , frame = cam.read()
#     # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     if not ret:
#         print("kameradan görüntü okunamıyor")
#         break
#     
#     cv2.imshow("AliSamiYen", frame)
# 
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("video kapatıldı")        
#         break
# cam.release()
# cv2.destroyAllWindows()
#=============================================================================







































