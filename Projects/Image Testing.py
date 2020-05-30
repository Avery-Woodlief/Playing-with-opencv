import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread("Resources/lizard.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (11, 11), 0)
imgCanny = cv2.Canny(img, 200, 150)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Can Image", imgCanny)
cv2.imshow("Dial Image", imgDialation)
cv2.imshow("Rode Image", imgEroded)





cv2.waitKey(0)