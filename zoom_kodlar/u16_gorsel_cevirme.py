import cv2 as cv

img=cv.imread(r'data/gol_manzarasi.jpeg')

yatay_img= cv.flip(img,1) #yatay öğrenme
dky_img= cv.flip(img,0) #yatay öğrenme
yzseksen_img=cv.flip(img,-1) # hem dikey hem yatay

cv.imshow("yatay", yatay_img)
cv.imshow("dikey", dky_img)
cv.imshow("180", yzseksen_img)

cv.waitKey(0)
cv.destroyAllWindows()

