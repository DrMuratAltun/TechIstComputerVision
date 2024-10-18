import cv2

# Görüntüyü yükleme
image = cv2.imread('yesil_elma.jpg')

# Görüntünün boyutlarını al (yükseklik, genişlik ve kanal sayısı)
height, width, channels = image.shape

# Görüntünün veri tipini al
data_type = image.dtype

# Bilgileri yazdır
print(f"Görüntü Yüksekliği: {height} piksel")
print(f"Görüntü Genişliği: {width} piksel")
print(f"Kanal Sayısı: {channels}")
print(f"Veri Tipi: {data_type}")

# Görüntüyü göster (isteğe bağlı)
cv2.imshow("Goruntu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
