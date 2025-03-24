import streamlit as st

def about_me():
    st.title("About the Creator")
    
    c1, c2 = st.columns([2, 1])  # Membuat kolom dengan rasio 2:1 untuk teks & gambar
    
    with c1:
        st.markdown("""
        **Halo!** Saya **Steven Graciano Immanuel Cahyono**, mahasiswa **Universitas Kristen Satya Wacana**.  
        
        Aplikasi ini adalah **Tugas Akhir** saya, yang bertujuan untuk **meningkatkan konsumsi ikan di Indonesia**.  
        Saat ini, konsumsi ikan di Indonesia masih rendah, padahal ikan kaya akan **protein, omega-3, dan kalsium**, yang sangat baik bagi kesehatan.  

        Dengan aplikasi ini, pengguna dapat **mengunggah / memotret gambar ikan**, lalu sistem akan **mengenali jenis ikan serta menampilkan informasi gizinya** secara otomatis.  
        
        """)
        
        st.markdown("📌 **GitHub:** [github.com/imanuelsteven](https://github.com/imanuelsteven)")  
        st.markdown("📌 **LinkedIn:** [linkedin.com/in/stevengraciano](https://www.linkedin.com/in/stevengraciano/)")  
        
    with c2:
        st.image("Assets\steven.jpg", use_container_width=True)  # Menampilkan gambar profil dengan ukuran yang sesuai
