import cv2

image = cv2.imread("phase 1 / image name if ")
if image is not None:
    cv2.imshow("image show", image )#open the window 
    cv2.waitkey(0)#wait for a key 
    cv2.destroyAllwindows()#close the world 

else:
    print("image could not loaded ")

