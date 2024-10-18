import cv2 as cv

# Kamera yakalamasını başlat
cap = cv.VideoCapture(0)

while True:
    # Her bir çerçeveyi sırayla yakala
    ret, frame = cap.read(0)

    # Elde edilen çerçeveyi göster
    cv.imshow('Kamera', frame)

    # Eğer 'q' tuşuna basılırsa döngüden çık
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
