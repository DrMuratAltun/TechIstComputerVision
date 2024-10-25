import cv2 as cv

#dosya oku
img=cv.imread(r'data/kizil_sac3.jpg')
#img_fer=cv.imread(r'data/kirmizi_ferrari.jpg')
img_fer=cv.imread(r'data/kirmizi_togg.jpg')

b,g,r=cv.split(img)
bf,gf,rf=cv.split(img_fer)

#mavi saç
img_mavi=cv.merge((r,g,b))

#mavi ferrari
mv_fer=cv.merge((rf,gf,bf))

#sari saç
sari_sac=cv.merge((b,r,r))


#laci ferrari
lc_fer=cv.merge((rf,gf,gf))

#Turkuaz
tr_fer=cv.merge((rf,rf,bf))

#Turkuaz
pembe_fer=cv.merge((rf,gf,rf))

#fotoyu göster
#cv.imshow('Orijinal saç', img)
#cv.imshow('Mavi sac', img_mavi)
#cv.imshow('Sari sac',sari_sac)
cv.imshow('Kirmizi ferrari',img_fer)
cv.imshow('Mavi ferrari',mv_fer)
cv.imshow('Laci ferrari',lc_fer)
cv.imshow('Tr ferrari',tr_fer)
cv.imshow('Pembe ferrari',pembe_fer)




cv.waitKey(0)
cv.destroyAllWindows()
