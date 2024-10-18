import cv2

# Görüntüyü yükle
image = cv2.imread('sehir_goruntusu.jpeg')  

# Yeni piksel boyutlarını belirle
new_width = 256  # Yeni genişlik
new_height = 192  # Yeni yükseklik
new_dimensions = (new_width, new_height)

# Görüntüyü yeniden boyutlandır
resized_image = cv2.resize(image, new_dimensions)

# Görüntüyü göster
cv2.imshow('Yeniden Boyutlandirilmis Goruntu', resized_image)
cv2.imwrite('kucuk_sehir_goruntusu.jpeg', resized_image)
# Pencereyi kapat
cv2.waitKey(0)
cv2.destroyAllWindows()
