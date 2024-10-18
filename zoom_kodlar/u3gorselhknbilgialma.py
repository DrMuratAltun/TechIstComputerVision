import cv2 as cv
#resmi oku
img=cv.imread(r'data/yesil_elma.jpg')

# görüntünün boyutlarını al (yüseklik ve genişlik)
print(img.shape)
#height,width,=img.shape[:2]
channels=img.shape[2]
print("Genişlik ve yükseklik:",img.shape[1],img.shape[0])

print (f'Görüntü yükseliği:{img.shape[0]}')
print(f'Görüntü genişliği:{img.shape[1]}')
print(f'Kanal sayısı:{img.shape[2]}')
print(f'Veri tipi:{img.dtype}')

#isteğe bağlı
cv.imshow('Elma',img)
cv.waitKey(0)
cv.destroyAllWindows()