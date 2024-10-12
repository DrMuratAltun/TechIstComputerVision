import cv2

# Resmi bir numpy dizisi olarak okur.
img = cv2.imread('satranc3x3.jpg')

#img içeriğini bir sayı dizisi olarak gösterir.
print(img) 



# Resmi başlıkla birlikte göster.
cv2.imshow('Resim', img)

# Bekle ve kapat.
cv2.waitKey(0)
cv2.destroyAllWindows()