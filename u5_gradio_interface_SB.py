import gradio as gr
import numpy as np
import cv2 as cv

def convert_img_gry(image):
    gray_img=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    return gray_img

#Gradio arayüzü oluştur
interface=gr.Interface(
    fn=convert_img_gry,
    inputs=gr.Image(type="numpy"),
    outputs="image",
    title="Gri Tonlamalı Resme Dönüştür",
    description="Bir görüntü yükleyin ve onu siyah beyaza çevirin"
)

#Uygulamayı çalıştır
if __name__== "__main__":
    interface.launch(share=True)