import cv2 as cv
import numpy as np

# Resmi bir numpy dizisi olarak okur (BGR)
img_bgr = cv.imread('elma.jpg')

# Orijinal resmi ekranda göster
cv.imshow('Kirmizi Elma', img_bgr)

# Resmi kanallarına ayır
b, g, r = cv.split(img_bgr)

# Kırmızı ve yeşil kanalları birleştir
img_new = cv.merge((b, r, g))

# Yeni resmi ekranda göster
cv.imshow('Yesil Elma', img_new)

#yeni_resim.jpg adlı bir dosya olarak kaydet
cv.imwrite('yesil_elma.jpg', img_new)

# Bekle ve kapat
cv.waitKey(0)
cv.destroyAllWindows()