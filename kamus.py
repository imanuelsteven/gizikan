import streamlit as st
import pandas as pd
import json


def kamus():
    st.title("Kamus Gizikan🐟")
    st.divider()

    # Load JSON
    with open("Kamus/Data Ikan/data_ikan.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Looping untuk menampilkan tiap ikan
    for idx, ikan in enumerate(data, start=1):
        st.header(f"{idx}. {ikan['nama']} ({ikan['nama_inggris']})")
        st.image(ikan["gambar"])

        # Expander Profil Ikan
        with st.expander("📌 Profil Ikan"):
            for key, value in ikan["profil"].items():
                st.write(f"**{key.capitalize()}**: {value}")

        # Expander Kandungan Gizi
        with st.expander("🍽️ Kandungan Gizi"):
            st.write("per 100g")
            df_gizi = pd.DataFrame(ikan["gizi"])
            st.dataframe(df_gizi)

        st.divider()  # Garis pemisah antar ikan


