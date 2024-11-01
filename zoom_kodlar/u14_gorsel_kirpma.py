import cv2 as cv

#resmi yükle
img=cv.imread(r'data/gol_manzarasi.jpeg')

cv.imshow('Gol Manzarasi',img)

cv.waitKey(0)
cv.destroyAllWindows()

#yükseklik ve genişlik
h,w=img.shape[:2]

#kırpılacak alanın başlangıç ve bitiş koordiatlaırnı
start_row,start_col=int(h*.25),int(w*.25)
end_row,end_col=int(h*.75),int(w*.75)

#resmi kırp
croppped_img=img[start_row:end_row,start_col:end_col] #dilimleme işlemi yap

cv.imshow('Kırpılmış resim',croppped_img)
cv.waitKey(0)
cv.destroyAllWindows()