import cv2
import numpy as np

# Görüntüleri yükle
img1 = cv2.imread('data/kirmizi_togg.jpg', 0)  # Gri tonlamalı olarak yükle
img2 = cv2.imread('data/mavi_togg.jpg', 0)

# ORB detektörünü başlat
orb = cv2.ORB_create()

# Anahtar noktaları ve tanımlayıcıları tespit et
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher nesnesi oluştur ve eşleşmeleri hesapla
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Eşleşmeleri mesafeye göre sırala
matches = sorted(matches, key=lambda x: x.distance)

# Eşleşmeleri çiz
result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# Sonucu göster
cv2.imshow('Feature Matching', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
