import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width, height = 250, 350

pts1 = np.float32([[87, 169], [221, 148], [118, 337], [273, 337]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Cards", img)
cv2.imshow("I/O", imgOutput)

cv2.waitKey(0)