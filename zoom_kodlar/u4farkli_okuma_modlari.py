#Farklı okuma modları
import cv2 as cv
resim_dosyasi=r'data/satranc3x3.jpg'

img_color=cv.imread(resim_dosyasi,1)
#img_color=cv.imread(resim_dosyasi,cv.IMREAD_COLOR)


#img_gray=cv.imread(resim_dosyasi,cv.IMREAD_GRAYSCALE)
img_gray=cv.imread(resim_dosyasi,0)

cv.imshow('Renkli',img_color)
cv.imshow('Siyah Beyaz', img_gray)
resim_dosyasi2=r'data/yesil_elma.jpg'
img2=cv.imread(resim_dosyasi2,0)

cv.imshow('Siyah Beyaz Elma',img2)

img3=cv.imread('data/andrewNG.png',0)
cv.imshow('Andrew Ng',img3)

cv.waitKey(0)
cv.destroyAllWindows()