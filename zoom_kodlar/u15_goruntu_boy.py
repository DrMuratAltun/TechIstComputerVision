import cv2 as cv
#dosya oku
img=cv.imread(r'data/gol_manzarasi.jpeg')
cv.imshow('Orijinal',img)

#resmi yeniden boyutlandır
#ölçeklendirme
fx,fy=.5,.5

resized_img=cv.resize(img,None,fx=fx,fy=fy) #,interpolation=cv.INTER_LINEAR
cv.imshow('Resized',resized_img)

cv.waitKey(0)  
cv.destroyAllWindows()