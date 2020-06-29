import numpy as np 
import cv2
# color in blue green red format

# geting image from disk
# img =cv2.imread('./data/lena.jpg',1)
 
#  getting image using numpy
img=np.zeros([512,512,3],np.uint8) 


img=cv2.line(img,(0,0),(255,255),(55,45,35),4)
img=cv2.arrowedLine(img,(0,0),(255,45 ),(55,45,35),4)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),10)
img=cv2.circle(img,(447,63),63,(0,255,0),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'opencv',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow ('imgage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
