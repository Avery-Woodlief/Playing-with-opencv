import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
img[200:300, 100:300] = 0, 255, 0

img2 = np.zeros((512, 512, 3), np.uint8)
print(img2.shape)
img[100:150, 200:300] = 255, 0, 0

img3 = np.zeros((512, 512, 3), np.uint8)
print(img3.shape)
img[0:50, 100:500] = 0, 0, 255

img4 = np.zeros((512, 512, 3), np.uint8)
print(img4.shape)
img[0:100, 50:200] = 255, 0, 255

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 255), 5)

cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

cv2.putText(img, " Hello World ", (40, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75, (250, 255, 100), 1)




cv2.imshow("Image", img)

cv2.waitKey(0)