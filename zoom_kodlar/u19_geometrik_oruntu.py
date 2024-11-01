import cv2
import numpy as np

# Boş bir tuval oluştur
tuval = np.ones((600, 600, 3), dtype="uint8") * 255

def draw_triangle(canvas, center, size, color):
    points = np.array([
        [center[0], center[1] - size],
        [center[0] - size, center[1] + size],
        [center[0] + size, center[1] + size]], np.int32)
    cv2.fillPoly(canvas, [points], color)

# Tuval üzerine geometrik şekilleri çiz
for i in range(0, 600, 40):  # Sütunlar
    for j in range(0, 600, 40):  # Satırlar
        # Kare çiz
        cv2.rectangle(tuval, (i, j), (i + 30, j + 30), (255 - j//5, 0, i//5), -1)

        # Üçgen çiz
        draw_triangle(tuval, (i + 20, j + 20), 15, (0, 255 - i//5, j//5))

        # Daire çiz
        cv2.circle(tuval, (i + 10, j + 10), 10, (i//5, j//5, 255), -1)

# Tuvali göster
cv2.imshow("Soyut Geometrik Desen", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()
