#Bu kod belirli bir örnekleme fakörü kullanarak resmi yeniden boyutlandırmaktadır.
import cv2

# Resmi yükle
img = cv2.imread('gol_manzarasi.jpeg')
cv2.imshow('Original Image', img)

# Ölçekleme faktörlerini belirle
fx, fy = 0.5, 0.5

# Resmi yeniden boyutlandır
resized_img = cv2.resize(img, None, fx=fx, fy=fy)

# Yeniden boyutlandırılmış resmi göster
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
