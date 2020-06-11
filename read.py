import cv2
import numpy as np

img = cv2.imread("./upload/moedas.jpg", 0)

test = np.array(img)
print(np.unique(test, axis=0, return_counts = True))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()