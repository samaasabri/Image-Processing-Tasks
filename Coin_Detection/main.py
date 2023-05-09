import cv2;
import numpy as np

img = cv2.imread('coins.jpg', -1)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low = np.array([0,50,50])

high = np.array([200, 255, 255])
segmented = cv2.inRange(hsv_img, low, high)

kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(segmented, kernel, iterations=5)

output = cv2.connectedComponents(img_erosion)
print(output)
cv2.imshow('coins', img_erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()