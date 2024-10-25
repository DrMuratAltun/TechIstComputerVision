import cv2 as cv
import numpy as np

#Giriş ve çıkış video
input_video=r'data/araba_video.mp4'
output_video=r'data/araba_output.mp4'

#video yakalama
cap=cv.VideoCapture(input_video)

#video özelliklerine bak
fourcc=cv.VideoWriter_fourcc(*'mp4v') #Kodek
fps=int(cap.get(cv.CAP_PROP_FPS)) #saniyedeki frame sayısı
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) #genislik
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) #yükseklik
#kodek=cap.get(cv.CAP_PROP_FOURCC)

out=cv.VideoWriter(output_video,fourcc,fps,(width,height)) #videoyumuzu belirtilen özellikelrde oluşturur

while cap.isOpened():
    ret,frame=cap.read()
    
    if not ret: #okuma başarılı ise
        break

    #renk kanallarını ayarla
    b,g,r=cv.split(frame)

    rgb_frame=cv.merge((b,r,r))
    cv.imshow('Mavi video',rgb_frame)

    out.write(rgb_frame) #videoya yaz
    if cv.waitKey(1) & 0xFF == ord('q'): #q tusuna basıldıgında
        break
cap.release()
out.release()
cv.destroyAllWindows()

