import cv2
resim_dosyasi="satranc3x3.jpg"

# Resmi bir numpy dizisi olarak okur (renkli)
img_color = cv2.imread(resim_dosyasi, cv2.IMREAD_COLOR)
#cv2.imread(resim_dosyasi,1)

# Resmi bir numpy dizisi olarak okur (siyah-beyaz)
img_gray = cv2.imread(resim_dosyasi, cv2.IMREAD_GRAYSCALE) 
#cv2.imread(resim_dosyasi,0)

# Resmi bir numpy dizisi olarak okur (alfa kanalı dahil)
img_alpha = cv2.imread(resim_dosyasi, cv2.IMREAD_UNCHANGED)
#cv2.imread(resim_dosyasi,-1)

# Resim içeriğini göster
print(img_color)
print(img_gray)
print(img_alpha)

# Resmi göster başlık ve resim
cv2.imshow('Renkli Resim', img_color)
cv2.imshow('Siyah-Beyaz Resim', img_gray)
cv2.imshow('Alfa Kanali Olan Resim', img_alpha)

# Bekle ve kapat
cv2.waitKey(0)
cv2.destroyAllWindows()