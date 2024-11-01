import cv2 as cv
img=cv.imread(r'data/monalisa.jpg')

cv.imshow('Orijinal', img)
print(img.shape[:2])
cv.line(img,(0,0),(534,720),(0,0,255), thickness=3)
cv.line(img,(534,0),(0,720),(0,0,255), thickness=3)
cv.putText(img,'Fake Mona Lisa', (140,360), cv.FACE_RECOGNIZER_SF_FR_COSINE,
            3, (255,0,0), 2)
cv.imshow('Cizgi Metin', img)

cv.waitKey(0)
cv.destroyAllWindows()  