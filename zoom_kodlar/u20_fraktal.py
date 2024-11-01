import cv2
import numpy as np

def draw_sierpinski_triangle(canvas, vertices, depth):
    if depth == 0:
        cv2.fillPoly(canvas, [np.array(vertices, dtype=np.int32)], (255, 0, 0))
    else:
        # Üçgenin orta noktalarını bul
        pt1 = ((vertices[0][0] + vertices[1][0]) // 2, (vertices[0][1] + vertices[1][1]) // 2)
        pt2 = ((vertices[1][0] + vertices[2][0]) // 2, (vertices[1][1] + vertices[2][1]) // 2)
        pt3 = ((vertices[2][0] + vertices[0][0]) // 2, (vertices[2][1] + vertices[0][1]) // 2)

        # Her kenarın orta noktasını kullanarak yeni üçgenler oluştur
        draw_sierpinski_triangle(canvas, [vertices[0], pt1, pt3], depth - 1)
        draw_sierpinski_triangle(canvas, [pt1, vertices[1], pt2], depth - 1)
        draw_sierpinski_triangle(canvas, [pt3, pt2, vertices[2]], depth - 1)

# Boş bir tuval oluştur
tuval = np.ones((600, 600, 3), dtype="uint8") * 255

# Başlangıç üçgeninin köşe noktalarını belirle
points = [(300, 50), (50, 550), (550, 550)]

# Sierpinski Üçgeni fraktalını çiz
draw_sierpinski_triangle(tuval, points, 5)  # Derinlik 5

# Tuvali göster
cv2.imshow("Sierpinski Triangle Fractal", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()
