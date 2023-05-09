import cv2;

img = cv2.imread('test.png', -1)
img_blur = cv2.blur(img, (3, 3))


edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

cv2.imshow('Bird', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()