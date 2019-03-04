import cv2
from PIL import Image

# a = cv2.imread('./log.png')
# cv2.imshow('img', a)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
a = Image.open('./test.jpg')
a.save('./test.jpeg')