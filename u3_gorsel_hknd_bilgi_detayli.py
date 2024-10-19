import cv2 as cv
#resmi al
img=cv.imread(r'data/yesil_elma.jpg')

yukseklik=img.shape[0]
genislik=img.shape[1]
kanal_sayisi=img.shape[2]

print ("----------Resim Özellikleri-----------")
print(f"Görsel genişlikxyükseklik:{genislik}x{yukseklik}")
print(f"Görsel Toplam piksel:{genislik*yukseklik}")
print (f"Görsel kanal sayısı:{kanal_sayisi}") 
#Renkli görseller için BGR 3 kanal bulundurur ve 3 elemanlı bir liste
#Gray scale de ise 1 kanal bulunur ve terk bir sayı 
#Her renkli piksel 3 elemanlı bir liste içerirken siyah beyaz resim pikseli tek bir sayıdır
# değerler 09-255 arasındadır
print('Veri türü:', img.dtype)

# size toplam eleman sayısı
#piksel sayısı * kanal sayısı
print("Eleman sayısı", img.size)
print ("Boyut:", img.size*img.itemsize) # veri tipi 1 Byte yer kaplıyor
print ("Bellekte kapladığı alan KB :", img.size*img.itemsize/1024)

import os 
dosya_boyutu=os.path.getsize(r'data/yesil_elma.jpg')
print ("Dosya Boyutu Diskte kapladığı alan:", dosya_boyutu/1024, "KB")

