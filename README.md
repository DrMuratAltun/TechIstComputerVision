# TechIstComputerVision

Bu repo, **Python + OpenCV + NumPy** ağırlıklı olarak hazırlanmış, temel ve orta seviye **bilgisayarlı görme / görüntü işleme** uygulamalarını içeren bir çalışma koleksiyonuudur.  
Ayrıca bazı örneklerde **Gradio** kullanılarak küçük web arayüzleri oluşturulmuştur.

Repo; görüntü okuma/yazma, piksel manipülasyonu, kırpma, yeniden boyutlandırma, döndürme, renk uzayı/kanal işlemleri, webcam akışı ve daha ileri örnekler olarak panorama, özellik benzerliği, fraktal/geometrik desen üretimi gibi konuları kapsar.

## Kurulum

### Gereksinimler
- Python 3.8+
- OpenCV
- NumPy
- (Bazı örnekler için) Gradio

`requirements.txt`:
- gradio
- opencv-python
- numpy

Kurulum:
```bash
pip install -r requirements.txt
```

## Repo Yapısı (Genel)

- **Kök dizin (root)**: Çeşitli “uygulama*.py / u*.py” örnekleri ve örnek görseller (jpg/png).
- **`zoom_kodlar/`**: Daha kapsamlı örneklerin toplandığı klasör.
  - `haarcascade_frontalface_default.xml`: Yüz tespiti gibi Haar Cascade örnekleri için.
  - `data/`: (içeriği ayrıca listelenmedi; bu klasör altında ek veri/görseller olabilir)
- **`src/`**: Şu an görünen tek içerik `readme.md` (boş/placeholder gibi duruyor).

> Not: Repoda çok sayıda örnek görsel (elma, araçlar, manzara/panorama vb.) bulunuyor. Bu görseller, ilgili script’lerde test verisi olarak kullanılıyor.

---

## Çalışmalar / Uygulamalar (Tek Tek)

Aşağıdaki açıklamalar dosya adlarından ve repodaki genel akıştan yola çıkarak hazırlanmıştır. İsterseniz her bir `.py` dosyasının içeriğini de tek tek okuyup README’ye “kod seviyesinde” daha net açıklamalar ekleyebilirim.

### 1) OpenCV kurulumu ve temel kontrol
- **`uygulama1_openCV_versiyon.py`**
  - OpenCV’nin yüklü olup olmadığını ve sürüm bilgisini kontrol etmeye yönelik başlangıç örneği.

### 2) Temel görsel işlemleri / görseli okuma-gösterme
- **`uygulama2_gorsel_islemleri.py`**
  - Görselin diskten okunması, ekranda gösterilmesi, temel I/O işlemleri.

- **`u2_gorsel_is_dilimleme.py`**
  - Görsel üzerinde “dilimleme/slicing” mantığı: NumPy indeksleme ile belirli bölgenin alınması gibi ROI (Region of Interest) yaklaşımı.

### 3) Görsel hakkında bilgi alma (boyut/kanal vb.)
- **`Uygulama3 Görsel hakkında bilgi alma.py`**
  - Bir görselin temel özellikleri: boyut (width/height), kanal sayısı, veri tipi gibi bilgileri inceleme.

- **`u3_gorsel_hknd_bilgi_detayli.py`**
  - Görsel bilgilerini daha detaylı gösteren/raporlayan sürüm.

### 4) Farklı okuma modları (renkli, gri vb.)
- **`uygulama 4 farklı okuma modları.py`** ve **`u4_farkli_okuma_mod.py`**
  - OpenCV’de `imread` okuma modları (renkli okuma, grayscale okuma vb.) ve farkların gözlenmesi.

### 5) Sayılardan görüntü üretme / matris tabanlı görüntü
- **`uygulama 5 sayıalrdan görüntüye.py`**
  - NumPy ile matris oluşturup bunu görüntü gibi görselleştirme; piksel değerleriyle görüntü üretmenin temeli.

### 6) Renk uzayı ve kanal dönüşümleri
- **`uygulama 6 renk uzayı dönüşümü.py`**
  - RGB/BGR → Gray gibi temel dönüşümler; `cvtColor` kullanımına giriş.

- (Ek örnekler)
  - **`u6_kirmizi_elma.py`**, **`u6_araba.py`**, **`u6_kizil_sac.py`**
  - Belirli renklerin (kırmızı tonları vb.) maskeleme/ayrıştırma veya renge dayalı manipülasyon örnekleri.

- **`u6_RenkDegistirmeGradio.py`**
  - Renk dönüşümü/renk değiştirme mantığını **Gradio arayüzü** ile kullanıcıdan görsel alıp çıktı üretme şeklinde sunan uygulama.

### 7) Renk bazlı örnek: kırmızı/yeşil elma ayrımı
- **`uygulama 7 kırmızı yeşil elma.py`**
  - Renk temelli segmentasyon/mask yaklaşımıyla kırmızı/yeşil nesneleri ayırma mantığı.

### 8) Araç görselleri üzerinde renk dönüşümü
- **`uygulama 8  araba renk dönüşümü.py`**
  - Araç görseli üzerinde belirli renklerin dönüştürülmesi/kanal işlemleri.

### 9) Dosya uzantısı / dosya adı ile çalışma
- **`uygulama 9_dosya_uzanti.py`**
  - Dosya uzantısı bulma/işleme (string/path işlemleri) gibi yardımcı bir örnek.

### 10) Kameradan görüntü akışı (webcam)
- **`uygulama 10 kameradana görüntü akışı.py`**
  - `VideoCapture` ile webcam’den canlı görüntü alma ve gösterme.

### 11) Piksellere erişim ve manipülasyon
- **`uygulama11 piksellere erişim ve manipülasyon.py`**
  - Piksel değerlerine doğrudan erişim, belirli bölgeleri değiştirme, basit manipülasyonlar.

### 12) Görsel kırpma (crop)
- **`uygulama 12 gorsel kirpma.py`**
  - ROI seçimi ve kırpma işlemi (NumPy slicing / OpenCV ile).

### 13) Görüntüyü yeniden boyutlandırma (resize)
- **`uygulama 13 görüntüyü yeniden boyutlandırma.py`**
  - `resize` ile ölçekleme, boyut değiştirme.

- **`uygulama 14 görüntüyü yenidnen boyutlandırma 2.py`**
  - Yeniden boyutlandırmanın alternatif yöntem/parametrelerle ikinci örneği.

### 15) Görseli döndürme (rotate)
- **`uygulama 15 görseli dondurme.py`**
  - Görsel döndürme (affine transform / rotate mantığı).

---

## `zoom_kodlar/` Klasörü (Daha geniş örnekler)

`zoom_kodlar` altında “u1...u23” şeklinde daha fazla örnek var. Görünen dosya adlarına göre içerikler:

- **`u1opencv_ver.py`**: OpenCV sürüm kontrolü
- **`u2gorsel_islemleri.py`**: Temel görsel işlemleri
- **`u3gorselhknbilgialma.py`**: Görsel hakkında bilgi
- **`u4farkli_okuma_modlari.py`**, **`u4v2_nostalji.py`**: Okuma modları + nostalji/filtre benzeri efekt denemesi
- **`u5kirmizielma.py`**: Kırmızı nesne/renk tabanlı maskeleme
- **`u6_renk_kanallari.py`**: Renk kanallarını ayırma/inceleme
- **`u7_dosya_uzantisi.py`**: Dosya uzantısı işlemleri
- **`u8_video_renkkanal.py`**: Video üzerinde kanal/renk işlemleri
- **`u9_web_cam.py`**, **`u10_webcam_sb.py`**: Webcam akışı örnekleri
- **`u11_web_renk_kanali.py`**: Webcam + renk kanalı/maskeleme
- **`u12_Gradio_filtre_uyg.py`**, **`u12v2_gradio_fdilter.py`**: Gradio ile filtre uygulaması
- **`u13piksel_man.py`**: Piksel manipülasyonu
- **`u14_gorsel_kirpma.py`**: Kırpma
- **`u15_goruntu_boy.py`**: Yeniden boyutlandırma
- **`u16_gorsel_cevirme.py`**: Görsel çevirme/flip
- **`u17_cizgi_metin.py`**: Görsele çizgi/metin çizme
- **`u18_geometrik_Sekiller.py`**, **`u19_geometrik_oruntu.py`**: Geometrik şekiller/desen üretimi
- **`u20_fraktal.py`**: Fraktal üretimi
- **`u21_ozellik_benzerlik_calismasi.py`**: Özellik çıkarımı/benzerlik (feature matching)
- **`u22_panorama.py`**: Panorama oluşturma (muhtemelen birden fazla görüntü birleştirme)
- **`u23_reg_of_in.py`**: ROI / region of interest temalı ileri bir örnek olabilir
- **`haarcascade_frontalface_default.xml`**: Haar Cascade ile yüz tespiti gibi model dosyası

---

## Örnek Çalıştırma

Genel olarak script’ler doğrudan çalıştırılabilir:
```bash
python uygulama12_gorsel_kirpma.py
```

Gradio içerenlerde:
```bash
python u6_RenkDegistirmeGradio.py
```
çalıştıktan sonra terminalde verilen yerel URL üzerinden arayüze erişilir.

---

## Lisans
Bu proje **MIT** lisansı ile lisanslanmıştır. Ayrıntı: `LICENSE`

## Yazar
- Dr. Murat Altun — https://github.com/DrMuratAltun