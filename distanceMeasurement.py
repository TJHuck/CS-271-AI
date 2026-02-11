##
## This was used to find the distance correspondance to pixels. 
## I used the football field as a known distance and used it to find that each pixel is 0.667 yards
## This file isn't needed once that info is known but I am keeping it to show the process
##

import cv2

## load image
img = cv2.imread("collegemap.png")

## use the football field to figure out distance to pixel correlation
## 53.3 yards wide and 100 yards long

top = [850,1305]
bottom = [850,1385]
left = [790,1350]
right = [940,1350]

vertical = 53.3/(bottom[1]-top[1])
horizontal = 100/(right[0]-left[0])
print("Up and down correspondance: "+str(vertical)+" yards per pixel")
print("Left and right correspondance: "+str(horizontal)+" yards per pixel")

cv2.circle(img,(top[0],top[1]),6,(0,0,255),-1)
cv2.circle(img,(bottom[0],bottom[1]),6,(0,0,255),-1)
cv2.circle(img,(left[0],left[1]),6,(0,0,255),-1)
cv2.circle(img,(right[0],right[1]),6,(0,0,255),-1)

cv2.imshow("map",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## after doing these calculations, we will assume that each pixel corresponds to 0.667 yards 
