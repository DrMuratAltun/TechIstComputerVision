import cv2 as cv

#imread fonksiyonu görsel okumak için kullanılır
img=cv.imread(r'data\satranc3x3.jpg')


print(img)
print (img[300:500,200:300])

# ikinci satırdaki kırmızı kareyi liste olarak al
#600x600 lük resim
kirmizi_kare=img[200:399,:199]
print (img[200:399,:199])

#imshow resmi göstermek için kullanılır
cv.imshow('kirmizi kare',kirmizi_kare)
cv.imshow('Satanç Görseli', img)
#görseli göster ve bekle 
#klavyeden bir tuşa basılınca 
cv.waitKey(0)
#pencereleri kapat
cv.destroyAllWindows()