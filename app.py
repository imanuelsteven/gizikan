import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image
import json
from Profile import about_me
from kamus import kamus
from Article import article
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# ============ 1. Konfigurasi Halaman (WAJIB PALING ATAS) ============
st.set_page_config(
    page_title="Gizikan",
    page_icon="🐟",
    layout="centered"
)

# ============ 2. Load Model & Data (Di-cache agar cepat) ============
@st.cache_resource
def load_model_and_labels():
    # Load model (Hanya dijalankan sekali saat app pertama buka)
    model = tf.keras.models.load_model('Modelling/Model/Gizikan_Model.h5')
    
    with open('Modelling/Model/model_labels.json', 'r') as file:
        class_labels = json.load(file)
    return model, class_labels

# Panggil fungsi load model
with st.spinner("Sedang memuat model AI..."):
    model, class_labels = load_model_and_labels()

# Load data nutrisi (Ringan, tidak perlu cache ketat tapi boleh saja)
with open('Kamus/Data Ikan/data_ikan.json', 'r', encoding='utf-8') as file:
    nutrisi_data = json.load(file)

# ============ 3. Styling CSS ============
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');
        .app-title {
            font-family: 'Poppins', sans-serif;
            font-size: 3.7rem !important;
            font-weight: 800;
            background: linear-gradient(120deg, #ffffff 0%, #a5f3fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.5rem;
            margin-top: 0rem !important;
            text-shadow: 0 0 30px rgba(165, 243, 252, 0.5);
        }
        
        .app-subtitle {
            text-align: center;
            color: rgba(255, 255, 255, 0.9);
            font-size: 1rem;
            font-weight: 500;
            margin-top: 0rem !important;
            margin-bottom: 1.5rem;
        }

        .kamus-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(120deg, #ffffff 0%, #a5f3fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: left;
        margin-bottom: 0rem !important; 
        text-shadow: 0 0 30px rgba(165, 243, 252, 0.5);
        }

        .kamus-subtitle {
            text-align: left;
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1rem;
            font-weight: 500;
            margin-top: 0rem !important;     
            margin-bottom: 0rem !important;    
        }

        .ikan-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem !important;
        margin-top: 0rem !important;
        }

        .informasi{
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.1rem !important;
        margin-top: 1rem !important;
        }

        .profile-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.3rem !important;
        font-weight: 800;
        background: linear-gradient(120deg, #ffffff 0%, #a5f3fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: left;
        margin-bottom: 0.1rem !important; 
        text-shadow: 0 0 30px rgba(165, 243, 252, 0.5);
        }

        .baca-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.3rem !important;
        font-weight: 800;
        background: linear-gradient(120deg, #ffffff 0%, #a5f3fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: left;
        margin-bottom: 0.3rem !important; 
        text-shadow: 0 0 30px rgba(165, 243, 252, 0.5);
        }

        .small-subheader {
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: rgba(255,255,255,0.9);
        }

        /* Sidebar Logo */
        [data-testid="stSidebar"] img {
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
            margin-bottom: 0rem;
        }

        /* Selectbox */
        .stSelectbox > div > div {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 11px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .sidebar-font {
            font-size: 26px !important;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            color: #FFFFFF;
        }

        body, .stText, .stMarkdown, .stTitle, .stHeader, .stCaption {
            color: #FFFFFF !important;
        }

        .block-container hr {
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
        }

        div[data-testid="stSidebarResizeHandle"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============ 4. Fungsi-fungsi Logika ============

def preprocess_image(img):
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img

def predict(image_file):
    img = Image.open(image_file)
    img_preprocessed = preprocess_image(img)
    preds = model.predict(img_preprocessed)
    class_index = np.argmax(preds)
    ikan_pred = class_labels[class_index]
    confidence = preds[0][class_index] * 100
    return ikan_pred, confidence

def tampilkan_info_ikan(nama_ikan_prediksi):
    st.markdown("---")
    st.markdown(f"<div class ='informasi'>Informasi Ikan Hasil Prediksi ℹ️</div>", unsafe_allow_html=True)

    ikan_terpilih = next((ikan for ikan in nutrisi_data if ikan["nama"].lower() == nama_ikan_prediksi.lower()), None)

    if ikan_terpilih:
        st.markdown(f"<div class='ikan-title'>{ikan_terpilih['nama']} ({ikan_terpilih['nama_inggris']})</div>",unsafe_allow_html=True)
        st.image(ikan_terpilih["gambar"])

        with st.expander("📌 Manfaat"):
             st.write(ikan_terpilih["manfaat"].get("manfaat", "-"))

        with st.expander("🍽️ Kandungan Gizi", expanded=True):
            st.write("per 100g")
            df_gizi = pd.DataFrame(ikan_terpilih["gizi"])
            # Mengubah index agar dimulai dari 1 (bukan 0)
            df_gizi.index = df_gizi.index + 1 
            st.dataframe(df_gizi)   
    else:
        st.warning("⚠️ Data ikan tidak ditemukan di kamus.")

# ============ 5. UI Utama ============
with st.sidebar:
    st.markdown('<p class="sidebar-font">Gizikan Profile</p>', unsafe_allow_html=True)
    
    # Pastikan gambar logo ada di folder Assets
    st.image("Assets/logo.png", use_container_width=True)
    
    st.markdown("---")
    
    # Perbaikan: Menggunakan st.markdown dengan baris baru (dua spasi di akhir) dan Link
    st.markdown(
        """ 
        **Author** : Steven Graciano Immanuel  
        **Hak Cipta** : Imanuelzteven  
        **LinkedIn** : [Steven Graciano](https://www.linkedin.com/in/stevengraciano/)
        """
    )

page = st.sidebar.selectbox("**Pilih Halaman**", ["🏠 Home", "🐟 Kamus Ikan", "ℹ️ Tentang Pembuat", "📘 Panduan Baca"])

# ============ Halaman ============
if page == "🏠 Home":
    # Header dengan styling modern
    st.markdown('<div class="app-title">🐟 Gizikan</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Aplikasi Prediksi Jenis Ikan dan Kandungan Gizinya!</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📸 Kamera", "📂 Unggah File"])

    with tab1:
        st.markdown(
        "<div class='small-subheader'>Ambil Gambar dengan Kamera 📸</div>",
        unsafe_allow_html=True)
        image_camera = st.camera_input("")

    with tab2:
        st.markdown(
        "<div class='small-subheader'>📂 Unggah Gambar Ikan dari File</div>",
        unsafe_allow_html=True)
        image_upload = st.file_uploader("", type=["jpg", "png", "jpeg"])

    # Prediksi dan tampilkan data
    image = image_camera if image_camera is not None else image_upload
    if image is not None:
        st.image(image, caption="Gambar yang Dipilih", use_container_width=True)

        with st.spinner("🔍 Memprediksi Kandungan Gizi..."):
            ikan_pred, confidence = predict(image)

        if confidence < 50:
            st.warning("🔍 Prediksi tidak dapat ditentukan karena tingkat kepercayaan kurang dari 50%. Silakan coba gambar lain yang lebih jelas.")
        else:
            st.success(f"🎯 Jenis Ikan: **{ikan_pred}** ({confidence:.2f}% yakin)")
            tampilkan_info_ikan(ikan_pred)

elif page == "🐟 Kamus Ikan":
    kamus()

elif page == "ℹ️ Tentang Pembuat":
    about_me()

elif page == "📘 Panduan Baca":
    article()