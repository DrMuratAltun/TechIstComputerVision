import cv2
import numpy as np
import gradio as gr

# Farklı filtre fonksiyonları
def apply_gaussian_blur(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)

def apply_sharpening_filter(frame):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(frame, -1, kernel)

def apply_edge_detection(frame):
    return cv2.Canny(frame, 100, 200)

def apply_invert_filter(frame):
    return cv2.bitwise_not(frame)

def adjust_brightness_contrast(frame, alpha=1.0, beta=50):
    return cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

def apply_grayscale_filter(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Filtre uygulama fonksiyonu
def apply_filter(filter_type, input_image=None):
    if input_image is not None:
        frame = input_image
    else:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            return "Web kameradan görüntü alınamadı"

    if filter_type == "Gaussian Blur":
        return apply_gaussian_blur(frame)
    elif filter_type == "Sharpen":
        return apply_sharpening_filter(frame)
    elif filter_type == "Edge Detection":
        return apply_edge_detection(frame)
    elif filter_type == "Invert":
        return apply_invert_filter(frame)
    elif filter_type == "Brightness":
        return adjust_brightness_contrast(frame, alpha=1.0, beta=50)
    elif filter_type == "Grayscale":
        return apply_grayscale_filter(frame)

# Gradio arayüzü
with gr.Blocks() as demo:
    gr.Markdown("# Web Kameradan Canlı Filtreleme")

    # Filtre seçenekleri
    filter_type = gr.Dropdown(
        label="Filtre Seçin",
        choices=["Gaussian Blur", "Sharpen", "Edge Detection", "Invert", "Brightness", "Grayscale"],
        value="Gaussian Blur"
    )

    # Görüntü yükleme alanı
    input_image = gr.Image(label="Resim Yükle", type="numpy")

    # Çıktı için görüntü
    output_image = gr.Image(label="Filtre Uygulandı")

    # Görüntü yüklendiğinde filtre uygulama fonksiyonu
    input_image.change(fn=apply_filter, inputs=[filter_type, input_image], outputs=output_image)

# Gradio arayüzünü başlat
demo.launch()
