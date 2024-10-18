import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('yesil_elma.jpg')

# Görüntü boyutlarını al
height, width = image.shape[:2]


# Beyaz kare için boyut ve başlangıç koordinatları
kare_boyutu = 50  # Örnek olarak 50x50 piksel
# Görüntünün ortasını bul.
baslangic_x = (width // 2)-25  
baslangic_y = (height // 2)-25

# Belirli bir bölgedeki pikselleri beyaza çevir
for y in range(baslangic_y, baslangic_y + kare_boyutu):
    for x in range(baslangic_x, baslangic_x + kare_boyutu):
        image[y, x] = [255, 255, 255]  # Beyaz renk

# Modifiye edilmiş görüntüyü gösterme
cv2.imshow("Modifiye Goruntu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
