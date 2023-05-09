import cv2
img1 = cv2.imread('I1.jpg', -1)
img2 = cv2.imread('I2.jpg', -1)
diff = img1-img2
result = img1 - diff
cv2.imshow('final', result)
cv2.waitKey(0)
cv2.destroyAllWindows()