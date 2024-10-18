import cv2

# Görüntüyü yükle
image = cv2.imread('kucuk_sehir_goruntusu.jpeg')

# Yatay çevirme
flipped_horizontally = cv2.flip(image, 1)

# Dikey çevirme
flipped_vertically = cv2.flip(image, 0)

# Görüntüleri göster
cv2.imshow('Orjinal Goruntu', image)
cv2.imshow('Yatay Cevrilmis Goruntu', flipped_horizontally)
cv2.imshow('Dikey Cevrilmis Goruntu', flipped_vertically)

# Pencereyi kapat
cv2.waitKey(0)
cv2.destroyAllWindows()
