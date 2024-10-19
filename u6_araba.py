# Renk kanallarını kullanarak elmanın rengini değiştireceğiz
import cv2 as cv
dosya_yolu=r'data/kirmizi_ferrari.jpg'
img_bgr=cv.imread(dosya_yolu)


b,g,r=cv.split(img_bgr)

# renk kanalarının değerini değiştir.
#kirmizilari yeşil yap
yesil_araba=cv.merge([b,r,g])
mavi_araba=cv.merge([r,g,b])
sari_araba=cv.merge([b,r,r])
mor_araba=cv.merge([r,g,r])
beyaz_araba=cv.merge([r,r,r])
sb_araba=cv.imread(dosya_yolu,0)
# orijinali göster
cv.imshow("Orijinal", img_bgr)

#değiştirilmiş yeşil
cv.imshow("Yesil", yesil_araba)

#değiştirilmiş mavi
cv.imshow("Mavi", mavi_araba)

#Sarı renkte bir araç
#değiştirilmiş mavi
cv.imshow("Sarı", sari_araba)

#değiştirilmiş mor
cv.imshow("Mor", mor_araba)

#değiştirilmiş beyaz
cv.imshow("Beyaz", beyaz_araba)

#Gri Tonlamalı
#Pencerelerin adı aynı olmamalı
cv.imshow("Gri Ton",sb_araba)

cv.waitKey()
cv.destroyAllWindows()