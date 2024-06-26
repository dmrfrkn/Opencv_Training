import cv2
import numpy as np
#paint yapımı


img = np.ones((512,512,3),np.uint8)

cizim = False
mod= False

def draw(event,x,y,flags,param):
    
    global cizim,xi,yi,mod
    
    if event == cv2.EVENT_LBUTTONDOWN:
        xi,yi, = x,y
        cizim = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if cizim == True:
            if mod:
                cv2.circle(img, (x,y), 10, (15,255,123),-1)
            else :
                cv2.rectangle(img, (xi,yi,),(x,y), (0,0,155),-1)
        else:
            pass
    elif event == cv2.EVENT_LBUTTONUP:
        cizim = False
        if mod:
            cv2.circle(img, (x,y), 10, (15,255,123),-1)
        else :
            cv2.rectangle(img, (xi,yi,),(x,y), (0,0,155),-1)
    
   # if event == cv2.EVENT_LBUTTONDBLCLK:
        
cv2.namedWindow("paint")        
cv2.setMouseCallback("paint",draw)       
        
        
while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("m"):
        mod = not mod
    

cv2.destroyAllWindows()            
        
        
