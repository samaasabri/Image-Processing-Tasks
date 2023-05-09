import cv2
img = cv2.imread('noisy_lena.png', -1)
median = cv2.medianBlur(img, 5)
avg = cv2.blur(img, (5, 5))
cv2.imshow('image', avg)
cv2.waitKey(0)
cv2.destroyAllWindows()