import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('data/gol_manzarasi.jpeg')

# ROI koordinatlarını belirle (x başlangıç, y başlangıç, genişlik, yükseklik)
x, y, w, h = 100, 100, 200, 200

# ROI'yi görüntüden kes
roi = image[y:y+h, x:x+w]

# ROI'yi göster
cv2.imshow("ROI", roi)

# ROI üzerinde bir işlem yap (örneğin, ROI'yi griye çevir)
roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# Gri ROI'yi orijinal görüntüye geri yerleştir (renkli olarak)
image[y:y+h, x:x+w] = cv2.cvtColor(roi_gray, cv2.COLOR_GRAY2BGR)

# Sonucu göster
cv2.imshow("Gri Olarak Modife", image)

# Maske oluştur
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)

# Maskeyi orijinal görüntü ile birleştir
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Sonucu göster
cv2.imshow("Maskeli Goruntu", masked_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

