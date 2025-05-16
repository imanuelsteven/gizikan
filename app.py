import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image
import json
from Profile import about_me
from kamus import kamus
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# ============ Load Model dan Data ============
model = tf.keras.models.load_model('Modelling/Model/Gizikan_Model.h5')

with open('Modelling/Model/model_labels.json', 'r') as file:
    class_labels = json.load(file)
    
with open('Kamus/Data Ikan/data_ikan.json', 'r', encoding='utf-8') as file:
    nutrisi_data = json.load(file)

# ============ Fungsi-fungsi ============

def preprocess_image(img):
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
    st.subheader("📋 Informasi Ikan Hasil Prediksi")

    ikan_terpilih = next((ikan for ikan in nutrisi_data if ikan["nama"].lower() == nama_ikan_prediksi.lower()), None)

    if ikan_terpilih:
        st.header(f"{ikan_terpilih['nama']} ({ikan_terpilih['nama_inggris']})")
        st.image(ikan_terpilih["gambar"])

        with st.expander("📌 Profil Ikan"):
            for key, value in ikan_terpilih["profil"].items():
                st.write(f"**{key.capitalize()}**: {value}")

        with st.expander("🍽️ Kandungan Gizi"):
            st.write("per 100g")
            df_gizi = pd.DataFrame(ikan_terpilih["gizi"])
            st.dataframe(df_gizi)
    else:
        st.warning("⚠️ Data ikan tidak ditemukan di kamus.")

# ============ UI Streamlit ============

st.set_page_config(
    page_title="Gizikan",
    page_icon="🐟",
    layout="centered"
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

        .title-font {
            font-size: 40px !important;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            text-align: left;
            color: #FFFFFF;
        }

        .sidebar-font {
            font-size: 30px !important;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            color: #FFFFFF;
        }

        body, .stText, .stMarkdown, .stTitle, .stHeader, .stCaption {
            color: #FFFFFF !important;
        }

        hr {
            border: 2px solid #FFFFFF;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown('<p class="sidebar-font">Gizikan Profile</p>', unsafe_allow_html=True)
    st.image("Assets/logo.png", use_container_width=True)
    st.markdown("---")
    st.write(
        """ 
        **Author** : **Steven Graciano Immanuel**  
        **Hak Cipta** : **Imanuelzteven**  
        **LinkedIn** : **Steven Graciano Immanuel**
        """
    )

page = st.sidebar.selectbox("**Pilih Halaman**", ["🏠 Home", "🐟 Kamus Ikan", "ℹ️ Tentang Pembuat"])

# ============ Halaman Utama ============
if page == "🏠 Home":
    st.title("🐟 Gizikan: Aplikasi Prediksi Jenis Ikan dan Kandungan Gizinya!")

    tab1, tab2 = st.tabs(["📸 Kamera", "📂 Unggah File"])

    with tab1:
        st.subheader("Ambil Gambar Ikan dengan Kamera 📸")
        image_camera = st.camera_input("")

    with tab2:
        st.subheader("📂 Unggah Gambar Ikan dari File")
        image_upload = st.file_uploader("", type=["jpg", "png", "jpeg"])

    # Prediksi dan tampilkan data

    image = image_camera if image_camera is not None else image_upload
    if image is not None:
        st.image(image, caption="Gambar yang Dipilih", use_container_width=True)

    # Tambahkan loading spinner saat prediksi berlangsung
    with st.spinner("🔍 Memprediksi Kandungan Gizi..."):
        ikan_pred, confidence = predict(image)

    if confidence < 50:
        st.warning("🔍 Prediksi tidak dapat ditentukan karena tingkat kepercayaan kurang dari 50%. Silakan coba gambar lain yang lebih jelas.")
    else:
        st.success(f"🎯 Jenis Ikan: **{ikan_pred}** ({confidence:.2f}% yakin)")
        tampilkan_info_ikan(ikan_pred)

# ============ Halaman Lain ============
elif page == "🐟 Kamus Ikan":
    kamus()

elif page == "ℹ️ Tentang Pembuat":
    about_me()

