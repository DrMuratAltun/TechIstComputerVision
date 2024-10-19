import cv2 as cv
#dosya yolunu tanımla
path_strnc=r'data/satranc3x3.jpg'
path_elma=r'data/elma.jpg'
#Renkli modda oku
img_color=cv.imread(path_strnc,cv.IMREAD_COLOR)
img_elma_color=cv.imread(path_elma,1)
#parametre değeri cv.IMREAD_COLOR yerine 1 de yazılabilir
#img_color=cv.imread(path_strnc,cv.1) 
#varsayılan değeri bu şekilde

#siyah beyaz modda oku
img_gry=cv.imread(path_strnc,0)
img_elma_gry=cv.imread(path_elma,cv.IMREAD_GRAYSCALE)

# 0 YERİNE cv.IMREAD_GRAYSCALE

# ciktiyi göster
cv.imshow("Renkli Cikti",img_color)
cv.imshow("kirmizi Elma",img_elma_color)
cv.imshow("SB Elma",img_elma_gry)
cv.imshow("Siyah Beyaz Ciktisi", img_gry)
#bir tuşa basılana kadar bekle
cv.waitKey(0)
cv.destroyAllWindows()

#Renkli fotoyu siyah beyaza çevirirken 
#Y=0.299R+0.587G+0.114B