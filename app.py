import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image
import json
from Profile import about_me
from kamus import kamus
from model_performance import model

# ======= Load Model & Data (DISABLE SEMENTARA) =======
# # Load fine-tuned model
# model = tf.keras.models.load_model('model_finetuned.h5')  # Ganti dengan model yang sudah fine-tuned

# # Load label kelas yang sesuai
# with open('labels.json', 'r') as file:
#     class_labels = json.load(file)

def preprocess_image(image):
    image = image.resize((224, 224))  # Resize sesuai model
    image = np.array(image) / 255.0   # Normalisasi
    image = np.expand_dims(image, axis=0)
    return image

# # Load data nutrisi dari JSON
# with open('nutrisi.json', 'r') as file:
#     nutrisi_data = json.load(file)

# def predict(image):
#     image = preprocess_image(image)
#     preds = model.predict(image)
#     class_index = np.argmax(preds)  # Ambil indeks prediksi tertinggi
#     ikan_pred = class_labels[str(class_index)]  # Cocokkan dengan label kelas
#     confidence = preds[0][class_index] * 100  # Persentase keyakinan
#     return ikan_pred, confidence

# def get_nutrition_data(ikan_pred):
#     return nutrisi_data.get(ikan_pred, {'Info': 'Data tidak ditemukan'})


# ======= UI Streamlit =======

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
    st.image("gizikan/Assets/logo.png", use_container_width =True)
    st.markdown("---")
    st.write(
        """ 
        **Author** : **Steven Graciano Immanuel**  
        **Hak Cipta**  : **Imanuelzteven**  
        **Linkedin**      : **Steven Graciano Immanuel**
        """
    )

# Sidebar navigation
page = st.sidebar.selectbox("**Pilih Halaman**", ["🏠 Home", "🐟 Kamus Ikan", "ℹ️ Tentang Pembuat", "📈 Perfoma Model"])

if page == "🏠 Home":
    st.title("🐟 Gizikan: Aplikasi Prediksi Jenis Ikan dan Kandungan Gizinya!")

    tab1, tab2 = st.tabs(["📸 Kamera", "📂 Unggah File"])

    with tab1:
        st.subheader("Ambil Gambar Ikan dengan Kamera 📸")
        image_camera = st.camera_input("")

    with tab2:
        st.subheader("📂 Unggah Gambar Ikan dari File")
        image_upload = st.file_uploader("", type=["jpg", "png", "jpeg"])

    # Menampilkan gambar yang diambil/upload
    image = image_camera if image_camera is not None else image_upload
    if image is not None:
        st.image(image, caption="Gambar yang Dipilih", use_container_width=True)
        st.write("### Prediksi: (Model Dinonaktifkan)")
        st.write("### Kandungan Gizi: (Model Dinonaktifkan)")
elif page == "🐟 Kamus Ikan" :
    kamus()
elif page == "ℹ️ Tentang Pembuat":
    about_me()
elif page == "📈 Perfoma Model" :
    model()
    


st.write("🚀 **Coming Soon:** Model prediksi ikan akan segera tersedia!") 
