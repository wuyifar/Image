import cv2
import numpy as np

# mask = cv2.imread('./log_black.png', cv2.IMREAD_GRAYSCALE)
mask = cv2.imread('./log.png')
print(mask.shape)
img = cv2.imread('./test1.jpg')

dilate = cv2.dilate(mask, None, iterations=1)

# dst = cv2.inpaint(img, dilate, 5, cv2.INPAINT_TELEA)

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        for channel in range(img.shape[2]):
            if mask[row, col, channel] == 0:
                val = 0
            else:
                reverse_val = 255 - img[row, col, channel]
                val = 255 - reverse_val * 256 / mask[row, col, channel]
                if val < 0: val = 0
            img[row, col, channel] = val




cv2.imshow('mask', mask)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
