import cv2

# Görüntüyü yükle
image = cv2.imread('yesil_elma.jpg')

# Görüntüyü farklı bir formatda kaydet
cv2.imwrite('yesil_elma.png', image) 