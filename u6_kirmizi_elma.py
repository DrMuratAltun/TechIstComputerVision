# Renk kanallarını kullanarak elmanın rengini değiştireceğiz
import cv2 as cv
img_bgr=cv.imread(r'data/elma.jpg')



b,g,r=cv.split(img_bgr)

# renk kanalarının değerini değiştir.
#kirmizilari yeşil yap
yesil_elma=cv.merge([b,r,g])
mavi_elma=cv.merge([r,g,b])
sb_elma=cv.imread(r'data/elma.jpg',0)
# orijinali göster
cv.imshow("Orijinal", img_bgr)

#değiştirilmiş yeşil
cv.imshow("Yesil", yesil_elma)

#değiştirilmiş mavi
cv.imshow("Mavi", mavi_elma)

#Gri Tonlamalı
#Pencerelerin adı aynı olmamalı
cv.imshow("Gri Ton",sb_elma)

cv.waitKey()
cv.destroyAllWindows()