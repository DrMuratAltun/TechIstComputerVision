import cv2 as cv
import numpy as np

tuval=np.ones((600,600,3),np.uint8)*255 # 3 kanallı boş bir tual oluşturuyor rengi: beyaz
#([255,255,255], [1,1,1])
cv.rectangle(tuval, (100, 100), (400, 400), (0, 0, 255), 5)
cv.circle(tuval, (300, 300), 100, (0, 255, 0), 5)

cv.imshow('Geometrk şekilller',tuval)
cv.waitKey(0)
cv.destroyAllWindows()