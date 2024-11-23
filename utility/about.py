import streamlit as st
import os

# CSS untuk animasi dengan delay bertahap
css = """
<style>
    .center-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin: 20px 0; /* Tambahkan margin atas dan bawah */
    }
    .content-description {
        text-align: justify;
        margin: 0 10px; /* Tambahkan margin untuk kenyamanan membaca */
    }
    @media only screen and (max-width: 768px) {
        .center-content {
            margin: 10px 0;
        }
        .content-description {
            margin: 0 5px;
        }
    }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Fungsi untuk menampilkan halaman dengan efek bertahap
def show_about_page():

        # Membuat layout kolom 
   with st.container():
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    st.image("./src/logo_buah (2).png", width=200)
    st.title("Freshty.id")
    st.markdown('</div>', unsafe_allow_html=True) 
    st.markdown("""
                <div style="text-align: justify;">
                <span>
                Freshty merupakan aplikasi yang dirancang untuk membantu konsumen dan petani dalam memantau kualitas buah secara praktis melalui analisis gambar. Dengan teknologi prediksi dan klasifikasi kualitas buah berbasis gambar, Freshty bertujuan untuk meningkatkan efisiensi supply chain dan membantu dalam proses pemilihan buah yang lebih cermat. Aplikasi ini tidak hanya memberikan manfaat bagi konsumen dalam kehidupan sehari-hari tetapi juga memberikan solusi cerdas bagi petani untuk meningkatkan perencanaan distribusi.  
                Dengan Freshty, baik konsumen maupun petani dapat lebih percaya diri dalam mengambil keputusan terkait penyimpanan, konsumsi, dan distribusi buah. Solusi ini diharapkan mampu mendukung proses supply chain yang lebih baik, mengurangi kerugian akibat buah yang cepat membusuk, dan memastikan pengalaman terbaik bagi setiap pengguna. Mari bergabung bersama kami untuk meningkatkan kualitas dan efisiensi dalam dunia buah-buahan! 🍎🍇🍌</span>
                </div>""", unsafe_allow_html=True)

    st.divider()
    # Layout untuk bagian penjelasan dan gambar
    col1, col2 = st.columns([3, 4])  

    with col1:
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.header("About Freshty")
        st.write("""

        **Fitur Utama:**
        - **Prediksi waktu distribusi:**   
            Aplikasi membantu petani merencanakan distribusi dengan memprediksi waktu maksimal buah dapat tetap segar berdasarkan tingkat kesegarannya.
        - **Rekomendasi penyimpanan selama pengiriman:**   
            Freshty memberikan rekomendasi lokasi penyimpanan yang sesuai selama proses pengiriman untuk menjaga kualitas buah tetap terjaga.
        - **Prediksi waktu pengiriman maksimal:**   
            Petani dapat mengetahui estimasi waktu pengiriman maksimal dalam hitungan hari agar buah tetap dalam kondisi segar hingga sampai ke konsumen.
        
        Dikembangkan dengan teknologi Machine Learning dan didukung dengan Streamlit, aplikasi ini bertujuan untuk mendukung rantai pasok buah yang 
        lebih efisien serta mengurangi limbah pangan.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.image("./src/gif/farm5.gif", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns([3, 2])  

    with col1:
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.image("./src/gif/farm2.gif", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.subheader("Sebelum Anda mengunggah...")
        st.markdown("> <span style='color:white'>Gambar yang dapat digunakan untuk klasifikasi sebaiknya berisi satu atau lebih dari buah-buahan berikut: </span>", unsafe_allow_html=True)
        st.markdown("""
                    1. Apel
                    2. Pisang
                    3. Mangga
                    4. Jeruk
                    5. Stroberi
                    """
                    )
        st.success('Anda tetap dapat mengunggah gambar lain, tetapi hasilnya mungkin tidak sesuai dengan harapan Anda.')
        st.markdown("<span style='color:white'>Kami merekomendasikan agar Anda mempersiapkan gambar dalam satu folder dan memberi nama setiap file dengan sesuai untuk mempermudah proses pengunggahan di bawah⬇️</span>", unsafe_allow_html=True)
        st.markdown("Terakhir, kami berharap Anda menikmati layanan kami, dan terima kasih telah memilih kami!🍏🍇🍌")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

# Panggil fungsi untuk menampilkan halaman 'About'
show_about_page()
