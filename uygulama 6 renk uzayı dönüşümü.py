import cv2

# Resmi bir numpy dizisi olarak okur (BGR)
img_bgr = cv2.imread('satranc3x3.jpg')

# Resmi RGB renk uzayına dönüştür
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Resimleri ekranda göster
cv2.imshow('BGR Resim', img_bgr)
cv2.imshow('RGB Resim', img_rgb)

# Bekle ve kapat
cv2.waitKey(0)
cv2.destroyAllWindows()