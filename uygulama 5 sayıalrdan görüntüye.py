import numpy as np
import cv2 as cv
# Satranç tahtası boyutları
rows = 3
cols = 3

# Satranç tahtası renkleri
color1 = [255, 255, 255]   # Beyaz (BMB)
color2 = [0, 0, 255]   # Kırmızı (MBM)

# Satranç tahtasını 0 lardan sayı dizisi olarak oluştur.
chessboard = np.zeros((rows*200, cols*200, 3), dtype=np.uint8)

# Satranç tahtasını renklendir
for i in range(rows):
    for j in range(cols):
        if (i+j) % 2 == 0:
            chessboard[i*200:(i+1)*200, j*200:(j+1)*200] = color1 
            #beyaz kareler belirleniyor
        else:
            chessboard[i*200:(i+1)*200, j*200:(j+1)*200] = color2
             #kırmızı kareler belirleniyor
# Satranç tahtasını ekrana yazdır
print(chessboard)

# Resmi ekranda göster
cv.imshow('Satranc Tahtasi', chessboard)

# Resmi "yeni_resim.jpg" adlı bir dosya olarak kaydet
cv.imwrite('yeni_resim.jpg', chessboard)

# Bekle ve kapat
cv.waitKey(0)
cv.destroyAllWindows()