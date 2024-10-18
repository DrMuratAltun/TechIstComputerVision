#kırmızı rengi yeşile çevirme
import cv2 as cv
img_bgr=cv.imread(r'data/elma.jpg')

#orijinali göster

b,g,r=cv.split(img_bgr)


#mavi renk
img_mavi=cv.merge((r,g,b))

#kırmızı ve yeşil kanalları birleştir
img_yesil=cv.merge((b,r,g))

#yeşil renkli elmayı göster
cv.imshow('Kırmızı elma', img_bgr)
cv.imshow('Mavi elma', img_mavi)
cv.imshow('Yeşil Elma', img_yesil)

cv.waitKey(0)
cv.destroyAllWindows() 

