import cv2

cam =cv2.VideoCapture(0)  #kamerayı tanımladık ve algılattık  


# cam.set(3,320) # kameranın boyutlarını ayarladık
# cam.set(4,240)   
if not cam.isOpened():#kameranın algılanıp algılanmadığını komtrol ettik
    print("kamera tanınmadı")
    exit()
while True:
    ret, frame = cam.read() # ret true ya da false deger döndürür 
    #kameradan goruntunun okunup okkunamadıgına dair bize bilgi verir
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
    if not ret:
        print("Kameradan görüntü okunamıyor")   
        break        
    cv2.imshow("kamera",frame)

    if cv2.waitKey(1)& 0xFF == ord("q"):
        print("görüntü sonlandırıldı")
        break

cam.release()#kameranın kapanması için bu kodu yazdık
cv2.destroyAllWindows() 