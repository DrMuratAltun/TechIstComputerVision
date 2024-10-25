import cv2 as cv

#kamerayı başlat
cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hvs_img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #hls_img=cv.cvtColor(frame,cv.COLOR_BGR2HLS)
    #rgba_img=cv.cvtColor(frame,cv.COLOR_BGR2RGBA)
    #rgb_img=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    #Görüntüyü yatay ve dikey  çevirme
    flipped_img=cv.flip(frame,-1)
    #0 dikey çevirme, 1 yatay, -1 de tersine
    cv.imshow('kamera ORG',frame)
    cv.imshow('kamera',flipped_img)
    cv.imshow('kamera gry',gray_frame)
    cv.imshow('kamera hvs',hvs_img)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

#kamerayı kapat
cap.release()
cv.destroyAllWindows()   
