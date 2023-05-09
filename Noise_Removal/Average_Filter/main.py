import cv2
img = cv2.imread('salt-pepper.jpg', -1)
blur = cv2.blur(img,(7,7))
cv2.imshow('AVERAG_Filter', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()