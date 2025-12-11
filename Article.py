import streamlit as st

def article():
    st.markdown('<div class="baca-title">Panduan Membaca Tabel Gizi</div>', unsafe_allow_html=True)
    st.write("Pahami arti nutrisi, jumlah zat gizi, dan % AKG agar bisa lebih bijak dalam memilih makanan.")
    st.markdown("---")

    st.markdown("### 💡 Apa Itu Nutrisi?")
    st.image('Tabel Gizi/Nutrisi.svg')

    st.markdown("""
    Nutrisi adalah **zat gizi** yang terkandung dalam makanan/minuman yang dibutuhkan tubuh untuk:
                
    * **⚡ Menghasilkan energi**
    * **🛡️ Menjaga sistem imun**
    * **🔧 Memperbaiki sel-sel tubuh**

    **Jenis nutrisi:**
    - **Makronutrien**: Protein, lemak, karbohidrat, kalori
    - **Mikronutrien**: Vitamin & mineral kayak vitamin A, B1, C, kalsium, dll

    **Contoh Analisis:**
    - **🥕 Vitamin A** = `0.655 mg (109.17% AKG)` → Super tinggi! Bagus buat mata & imun
    - **🍚 Karbohidrat total** = `0 mg` → Artinya produk ini bukan sumber karbo
    """)
    
    st.markdown("---")

    st.markdown("### 🍽️ Apa Itu Jumlah (per 100g)?")
    st.image('Tabel Gizi/Jumlah.svg')
    st.markdown("""
    Nilai di tabel adalah kandungan **per 100 gram** produk. Jadi, kalo kamu makan 200g, tinggal dikali 2 aja.

    Contoh dari label:
    - **Energi: 144 kkal** per 100g
    - **Lemak: 4.90 g** per 100g → tergolong sedang

    ⚠️ *Tips:* Makin besar porsi yang kamu makan, makin besar juga zat gizinya yang masuk ke tubuh.
    """)

    st.markdown("---")

    st.markdown("### 📈 Apa Itu % AKG (Angka Kecukupan Gizi)?")
    st.image('Tabel Gizi/AKG.svg')

    st.markdown("""
    **% AKG** = Persentase kebutuhan harian kamu yang terpenuhi dari 100g produk itu.

    Contoh:
    - **Vitamin B1**: `24%` → sekali makan 100g udah nyumbang hampir 1/4 kebutuhan vitamin B1 harianmu
    - **Kalsium**: `0.73%` → rendah banget, bukan sumber utama kalsium

    **Panduan umum Angka Kebutuhan Gizi (AKG):**
    - **< 5%** = rendah
    - **5–19%** = sedang
    - **≥ 20%** = tinggi

    AKG biasanya dihitung berdasarkan kebutuhan 2.150 kkal per hari (standar orang Indonesia dewasa).
    """)
    
    st.markdown("---")
    st.info("Dengan ngerti cara baca label gizi, kamu bisa milih makanan yang sesuai sama kebutuhan harianmu. Yuk jadi smart consumer! 💪🥦")
