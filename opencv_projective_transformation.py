import cv2
import numpy as np

img = cv2.imread("Ferrari16.jpg")

cv2.namedWindow("img",cv2.WINDOW_NORMAL )

print(img.shape)

rows,cols = img.shape[:2]

dst_points = np.float32([[0,0],
                         [cols-1,0],
                         [0,rows-1],
                         [cols-1,rows-1]])

click_count = 0
a = []
def draw(event,x,y,flags,param):
    global click_count, a
    
    if click_count<4 :
        
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print(click_count)
            print(x,y)
            click_count +=1
            a.append((x,y))
    else:
       
        # src = np.float32([a[0][0],a[0][1],a[1][0],a[1][1],
        #                   a[2][0],a[2][1],a[3][0],a[3][1]])## burası error veriyor?
        src = np.float32([a[0], a[1], a[2], a[3]])
        click_count = 0
        a = []
        
        
        M = cv2.getPerspectiveTransform(src, dst_points)   
        img_output = cv2.warpPerspective(img, M, (cols,rows))
        cv2.imshow("output",img_output)
        
        

# =============================================================================
# #noktanın ilk konumu
# src_points = np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
# 
# ##hedef noktalar
# dst_points = np.float32([[0,0],[cols-1,0],[int((cols-1)*0.33),rows-1],
#                          [int((cols-1)*0.66),rows-1]])
# 
# 
# projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
# 
# img_output = cv2.warpPerspective(img, projective_matrix, ((cols,rows)))
# 
# =============================================================================
cv2.setMouseCallback("img",draw)



while(1):
    cv2.imshow("img",img)
    # cv2.imshow("img_output",img_output)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()