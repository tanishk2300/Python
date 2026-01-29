import cv2

image=cv2.imread("phase 1 / image name ")

if image is not None:
    grey =cv2.cvtColor(image,cv2.COLOR_BGR2GREY)#change the colour of image 
    cv2.imshow("grey scale image",grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not load the image ")