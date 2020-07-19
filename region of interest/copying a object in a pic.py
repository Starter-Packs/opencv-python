# there is picture of messi hitting a ball and thar ball is copied to the side

import numpy as np
import cv2
img=cv2.imread('./data/messi5.jpg')
print(img.shape)
ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
