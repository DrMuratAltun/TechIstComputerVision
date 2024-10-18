import cv2 as cv
#imread fonksiyonu görseli okuyareak sayı dizisi şeklinde alır
img=cv.imread('data/satranc3x3.jpg')
print(img)

#sayı dizisini tekrar görsel oalrak gösterelim
cv.imshow('Stranc 3x3 @TechIst',img)
#print(img[300:400, :]) belirli bir kısmı göster
#bekle ve klavyeden bir tuşa basıldığında çık
cv.waitKey(0)
cv.destroyAllWindows()