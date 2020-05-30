import cv2
import numpy as np

img = cv2.imread("Resources/lizard.jpg")
print(img.shape)


imgResize = cv2.resize(img, (320, 240))
print(imgResize.shape)

imgCropped = img[0:100, 100:200]
print(imgCropped.shape)

imgCropped2 = img[0:200, 300:500]
print(imgCropped2.shape)



cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Piece 1", imgCropped)
cv2.imshow("Image Piece 2", imgCropped2)



cv2.waitKey(0)