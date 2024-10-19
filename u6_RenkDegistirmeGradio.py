import cv2 as cv
import gradio as gr
import numpy as np

def change_image_color(img, option, color_from=None, color_to=None):
    # Orijinal görüntüyü oku
    img_bgr = img.copy()

    if option == "R-G (Kırmızı Yeşile)":
        # Kırmızıları yeşil yap
        b, g, r = cv.split(img_bgr)
        new_img = cv.merge([b, r, g])
        return new_img
    elif option == "G-R (Yeşil Kırmızıya)":
        # Yeşili kırmızıya çevir
        b, g, r = cv.split(img_bgr)
        new_img = cv.merge([b, g, r])
        return new_img
    elif option == "R-B (Kırmızı Maviye)":
        # Kırmızıyı maviye çevir
        b, g, r = cv.split(img_bgr)
        new_img = cv.merge([r, g, b])
        return new_img
    elif option == "Gri Tonlamalı":
        # Gri tonlamalı görüntü
        gray_img = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
        return cv.cvtColor(gray_img, cv.COLOR_GRAY2RGB)
    elif option == "Özel Renk Dönüşümü" and color_from is not None and color_to is not None:
        # Belirli bir rengi başka bir renge dönüştür
        color_from_bgr = [int(color_from[i:i+2], 16) for i in (1, 3, 5)]
        color_to_bgr = [int(color_to[i:i+2], 16) for i in (1, 3, 5)]
        lower_bound = np.array(color_from_bgr, dtype="uint8")
        upper_bound = lower_bound
        mask = cv.inRange(img_bgr, lower_bound, upper_bound)
        img_bgr[mask != 0] = color_to_bgr
        return img_bgr
    else:
        # Orijinal görüntü
        return img_bgr

# Gradio arayüzü tanımla
interface = gr.Interface(
    fn=change_image_color,
    inputs=[
        gr.Image(type="numpy", label="Resim Yükleyin"),
        gr.Dropdown(["Orijinal", "R-G (Kırmızı Yeşile)", "G-R (Yeşil Kırmızıya)", "R-B (Kırmızı Maviye)", "Gri Tonlamalı", "Özel Renk Dönüşümü"], label="Dönüşüm Seçin"),
        gr.ColorPicker(label="Dönüştürülecek Renk"),
        gr.ColorPicker(label="Yeni Renk")
    ],
    outputs="image",
    title="Renk Dönüştürme Aracı",
    description="Resmin rengini dönüştürmek için bir seçenek belirleyin ve isterseniz belirli bir rengi başka bir renge dönüştürün."
)

# Arayüzü başlat
interface.launch()
