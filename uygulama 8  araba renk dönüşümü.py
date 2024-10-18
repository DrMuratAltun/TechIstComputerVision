import cv2 as cv
import numpy as np

# Resmi oku
img = cv.imread('kirmizi_togg.jpg')

#Orijinal araba
cv.imshow('Orijinal Araba', img)

# Resmi BGR formatından kopyala
b, g, r = cv.split(img)




#Yeşil arabayı Göster
img_green=cv.merge((b,r,g))
cv.imshow('Yesil Araba', img_green)

#mavi araba
img_blue = cv.merge((r, g, b))

#mavi arabayı göster
cv.imshow('Mavi Araba', img_blue)
cv.imwrite('mavi_togg.jpg',img_blue)

# Sarı renk, kırmızı ve yeşilin yüksek olduğu bir renktir.
# Bu nedenle, kırmızı ve yeşil kanallarını aynı seviyeye getiririz.
g = r  # Yeşil kanalını, kırmızı kanalıyla aynı yap

# Kanalları birleştir
img_yellow = cv.merge((b, g, r))

# Sarı arabayı göster
cv.imshow('Sari Araba', img_yellow)


cv.waitKey(0)
cv.destroyAllWindows()
