import cv2
import numpy as np


image_path = r'C:\Users\Administrator\Desktop\test.jpg'

img = cv2.imread(image_path)
width, height = img[0:2]
print(img)
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow("image", hsv)

thresh = cv2.inRange(img, np.array([170, 170, 170]), np.array([210, 210, 210]))
dilate = cv2.dilate(thresh, None, iterations=3)
cv2.imshow("a", dilate)
ercode = cv2.erode(dilate, None, iterations=4)
cv2.imshow("b", ercode)
ercode = cv2.erode(ercode, None, iterations=3)
cv2.imshow("b", ercode)
dilate2 = cv2.dilate(ercode, None, iterations=23)
cv2.imshow("c", dilate2)
# scan = np.ones((3, 3), np.uint8)
# cor = cv2.dilate(thresh, scan, iterations=3)
specular = cv2.inpaint(img, dilate2, 5, flags=cv2.INPAINT_TELEA)
# cv2.namedWindow("image", 0)
# cv2.resizedWindow("image", int(width/2), int(height/2))

cv2.imshow("image", specular)
cv2.imwrite('./test.jpg',specular)
cv2.waitKey(0)
cv2.destroyAllWindows()
