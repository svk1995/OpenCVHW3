import cv2

img = cv2.imread('C:/Users/Shachi/Downloads/OpenCV_Preperation/OpenCV_homework/Test_images/baboon.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('InputImage', cv2.WINDOW_AUTOSIZE)
cv2.imshow('InputImage',img)
cv2.imwrite('InputImage.png',img)

threshold_type = 2
threshold_value = 128
th, dst = cv2.threshold(gray, threshold_value, 255, threshold_type);
cv2.imshow('Thresholded Image',dst)
cv2.imwrite('Thresholded Image.png',dst)

current_threshold = 128
max_threshold = 255
th, thresholded = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY);
cv2.imshow('Binary threshold',thresholded)
cv2.imwrite('Binary threshold.png',thresholded)

threshold1 = 27
threshold2 = 125
cv,binary_image1=cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY)
cv,binary_image2=cv2.threshold(gray, threshold2, max_threshold, cv2.THRESH_BINARY_INV)
band_thresholded_image=cv2.bitwise_and( binary_image1, binary_image2)
cv2.imshow('Band Thresholding', band_thresholded_image)
cv2.imwrite('Band Thresholding.png', band_thresholded_image)

cv,semi_thresholded_image=cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
semi_thresholded_image=cv2.bitwise_and( gray, semi_thresholded_image)
cv2.imshow('Semi Thresholding', semi_thresholded_image)
cv2.imwrite('Semi Thresholding.png', semi_thresholded_image)

adaptive_thresh=cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 )
cv2.imshow('Adaptive Thresholding', adaptive_thresh)
cv2.imwrite('Adaptive Thresholding.png', adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

