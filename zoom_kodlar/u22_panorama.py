import cv2
import numpy as np

# Görüntüleri yükle
img1 = cv2.imread('data/panorama1.jpg')
img2 = cv2.imread('data/panorama2.jpg')

# ORB detektörünü kullan
orb = cv2.ORB_create()

# Anahtar noktaları ve tanımlayıcıları bul
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher ile eşleşmeleri bul
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# İyi eşleşmeleri filtrele
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append(m)

# Homografi matrisini hesapla ve panoramayı oluştur
if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Eğer homografi matrisi başarılı bir şekilde hesaplandıysa
    if M is not None:
        # İlk görüntüyü dönüştür
        h1, w1, _ = img1.shape
        h2, w2, _ = img2.shape
        result = cv2.warpPerspective(img1, M, (w1 + w2, max(h1, h2)))

        # İkinci görüntüyü sonuca ekle
        result[0:h2, w1:w1+w2] = img2

        # Sonucu göster
        cv2.imshow('Panorama', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Homografi matrisi hesaplanamadı.")
else:
    print("Yeterli iyi eşleşme bulunamadı.")