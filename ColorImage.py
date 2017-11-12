import cv2
import numpy as np

img = cv2.imread('C:/Users/Shachi/Downloads/OpenCV_Preperation/OpenCV_homework/Test_images/baboon.jpg')
cv2.namedWindow('OrginalImage', cv2.WINDOW_AUTOSIZE)
cv2.imshow('OriginalImage',img)

r,g,b = cv2.split(img)
cv2.imshow('Red', b)
cv2.imwrite('Red.png', b)
cv2.imshow('Green', g)
cv2.imwrite('Green.png', g)
cv2.imshow('Blue', r)
cv2.imwrite('Blue.png', r)
img[20,25] 

#e,f,g = cv2.split(img)
#cv2.cvtColor(src, ycrcb_image, CV_BGR2YCrCb);
img1=cv2.cvtColor(img,cv2.COLOR_RGB2YCR_CB) 
e,f,g = cv2.split(img1)
cv2.imshow('Y',   e)
cv2.imwrite('Y.png',   e)
cv2.imshow('Cb',  f)
cv2.imwrite('Cb.png',  f)
cv2.imshow('Cr',  g)
cv2.imwrite('Cr.png',  g)
img1[20,25]

img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
l,m,n = cv2.split(img2)
cv2.imshow('Hue',   l)
cv2.imwrite('Hue.png',   l)
cv2.imshow('Saturation',   m)
cv2.imwrite('Saturation.png',   m)
cv2.imshow('Value',   n)
cv2.imwrite('Value.png',   n)
img2[20,25]
cv2.waitKey(0)
cv2.destroyAllWindows()
