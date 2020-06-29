import numpy as np 
import cv2

img =cv2.imread('./data/lena.jpg',0)

cv2.imshow ('imgage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
