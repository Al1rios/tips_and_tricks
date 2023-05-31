
import cv2 as cv

img = cv.imread('school_viera.png')

img1 = cv.imshow('Original', img)

cv.waitKey(5)

grayed_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img2 = cv.imshow('grayed_image', grayed_img)

cv.waitKey(5000)

cv.imwrite('grayed.jpg', grayed_img)