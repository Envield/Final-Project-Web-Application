import streamlit as st
from utils import predict_freshness, get_farmer_recommendations

def show_farmer_page():
    st.title("Fitur Petani")

    st.image("./src/gif/farm3.gif", use_column_width=True)

    # CSS untuk styling "card"
    st.markdown(
        """
        <style>
        .card {
        background-color: #06061E;
        border: 1px solid #06061E;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease-in-out;
        }

        .card:hover {
        transform: translateY(-10px);
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write(
        """
        > Mendukung petani dalam merencanakan distribusi buah yang lebih efisien berdasarkan tingkat kesegaran buah. Berdasarkan gambar yang diunggah atau diambil, sistem memprediksi tingkat kesegaran dan memberikan rekomendasi terkait waktu distribusi serta penyimpanan selama pengiriman. Fitur ini membantu petani memastikan buah tetap segar ketika sampai di pasar atau pelanggan.
        """
    )

    with st.expander("**Fitur Utama**"):
        st.write("""
        1. Prediksi Tingkat Kesegaran Buah: Menyediakan estimasi tingkat kesegaran buah untuk membantu perencanaan distribusi.
        2. Rekomendasi Waktu Distribusi: Berdasarkan kondisi kesegaran, aplikasi memperkirakan waktu terbaik untuk mengirimkan buah agar kualitas tetap optimal.
        3. Prediksi Durasi Penyimpanan Selama Pengiriman: Menyediakan estimasi durasi maksimal buah dapat disimpan dalam kondisi pengiriman.
        4. Rekomendasi Lokasi Penyimpanan: Memberikan saran terkait tempat penyimpanan selama pengiriman berdasarkan tingkat kesegaran buah untuk memastikan buah tetap segar.
        
        """)

    with st.expander("**Prasyarat Penggunaan**"):
        st.write("""
        - Gambar buah yang diambil atau diunggah harus berkualitas baik dan jelas agar sistem dapat memprosesnya dengan akurat.
        - Aplikasi perlu diizinkan mengakses kamera atau penyimpanan, bergantung pada metode pengambilan gambar.
        
        """)

    with st.expander("**Langkah Penggunaan**"):
        st.write("""
        1. Pilih tab Petani di aplikasi.
        2. Pilih metode pengambilan gambar, upload foto untuk mengunggah gambar buah dari perangkat atau Ambil foto untuk memotret langsung.
        3. Jika menggunakan Upload foto, pilih gambar yang sesuai dari penyimpanan perangkat. Jika memilih Ambil foto, arahkan kamera ke buah yang akan dievaluasi, ambil foto, dan tekan tombol Simpan Foto untuk menyimpannya.
        4. Aplikasi akan menampilkan hasil prediksi, termasuk jenis buah, tingkat kesegaran, rekomendasi waktu distribusi, prediksi durasi penyimpanan selama pengiriman, dan rekomendasi lokasi penyimpanan.
        5. Semua hasil analisis akan ditampilkan dalam card sehingga memudahkan petani untuk melihat informasi terkait.
        
        """)

    option = st.selectbox("Pilih pengambilan gambar", ["Upload foto", "Ambil foto"])
    images_to_process = []

    if option == "Upload foto":
        uploaded_images = st.file_uploader("Upload gambar buah", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="farmer_upload")
        if uploaded_images:
            images_to_process.extend(uploaded_images)

    elif option == "Ambil foto":
        camera_image = st.camera_input("Ambil gambar dari kamera", key="farmer_camera")
        if camera_image:
            if "captured_images_farmer" not in st.session_state:
                st.session_state["captured_images_farmer"] = []
            if st.button("Simpan Foto"):
                st.session_state["captured_images_farmer"].append(camera_image)
                st.success("Foto berhasil disimpan!")
            images_to_process.extend(st.session_state["captured_images_farmer"])

    if images_to_process:
        col1, col2, col3 = st.columns(3)
        columns = [col1, col2, col3]

        for idx, image in enumerate(images_to_process):
            col = columns[idx % 3]
            with col:
                # Prediksi kesegaran buah
                freshness, fruit_type = predict_freshness(image)

                # Mendapatkan rekomendasi khusus petani
                distribution_time, max_delivery_time, storage_suggestion = get_farmer_recommendations(freshness, fruit_type)

                with col.container():
                    st.image(image, caption=f"Gambar {idx + 1}", use_column_width=True)

                    # Menampilkan informasi dalam format "card" yang disesuaikan untuk petani
                    st.markdown(
                        f"""
                        <div class="card">
                            <h5>Jenis Buah: {fruit_type}</h5>
                            <p><strong>Tingkat Kesegaran:</strong> {freshness:.2f}%</p>
                            <h6>Prediksi Distribusi (Tanpa Penyimpanan Proper)</h6>
                            <p>Buah disarankan didistribusikan dalam waktu: <strong>{distribution_time}</strong></p>
                            <h6>Durasi Maksimum Pengiriman</h6>
                            <p>Buah dapat bertahan hingga: <strong>{storage_suggestion}</strong> dalam pengiriman</p>
                            <h6>Rekomendasi Penyimpanan Selama Pengiriman</h6>
                            <p>{max_delivery_time}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
