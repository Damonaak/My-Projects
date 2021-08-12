import cv2

img_location = 'C:/Users/hp/Desktop/sketch/'
filename = 'kriti.jpg'

img = cv2.imread(img_location+filename)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

blur_image = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

inverted_blur_image = 250 - blur_image

pencil_sketch_img =cv2.divide(gray_image, inverted_blur_image, scale=256.0) 

cv2.imshow('Orignal image', img)
cv2.imshow('Grey Image', inverted_gray_image)
cv2.imshow('blur image', pencil_sketch_img)
cv2.waitKey(0)