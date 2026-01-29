import cv2
image = cv2.imread("phase1 / python_image.png")
if image is not None:
    succes=cv2.imread("output_python .png ",image)
    if succes:
        print("image saved succesfully 'give file name'")
    else:
        print("fail to save the image ")
else:
    print("error image could not be loaded")