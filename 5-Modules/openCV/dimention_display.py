import cv2
image=cv2.imread("phase 1/pyhon_image.png")
if image is not None:
    h,w,c=image.shape
    print("image loaded \n,height={h}\nwidth={w}\n,channal={c}")
else:
    print("could not be loaded ")
