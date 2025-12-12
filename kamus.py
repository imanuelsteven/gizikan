import streamlit as st
import pandas as pd
import json


def kamus():
    st.markdown('<div class="kamus-title">Kamus Ikan</div>', unsafe_allow_html=True)
    st.markdown('<div class="kamus-subtitle">Page ini berfungsi untuk mengetahui jenis-jenis ikan yang dapat di prediksi dan kandungan gizinya.</div>', unsafe_allow_html=True)

    st.divider()

    # Load JSON
    with open("Kamus/Data Ikan/data_ikan.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Looping untuk menampilkan tiap ikan
    for idx, ikan in enumerate(data, start=1):
        st.markdown(f"<div class='ikan-title'>{idx}. {ikan['nama']} ({ikan['nama_inggris']})</div>", unsafe_allow_html=True)
        st.image(ikan["gambar"])

        # Expander Profil Ikan
        with st.expander("📌 Manfaat"):
             st.write(ikan["manfaat"].get("manfaat", "-"))

        # Expander Kandungan Gizi
        with st.expander("🍽️ Kandungan Gizi"):
            st.write("per 100g")
            df_gizi = pd.DataFrame(ikan["gizi"])
            # Mengubah index agar dimulai dari 1 (bukan 0)
            df_gizi.index = df_gizi.index + 1 
            st.dataframe(df_gizi)

        st.divider()  # Garis pemisah antar ikan


