import streamlit as st
from utils import predict_freshness, get_consumer_recommendations

def show_consumer_page():
    st.title("Fitur Konsumen")

    st.image("./src/gif/Fruit.gif", use_column_width=True)

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
        > Memungkinkan pengguna (konsumen buah) untuk memprediksi tingkat kesegaran buah yang mereka beli atau miliki. Berdasarkan gambar yang diunggah atau diambil, sistem akan mengklasifikasikan jenis buah, menentukan tingkat kesegaran, dan memberikan rekomendasi yang berkaitan dengan konsumsi dan penyimpanan buah tersebut. Fitur ini membantu konsumen memaksimalkan masa konsumsi buah dan menyimpannya dalam kondisi terbaik.
        """
    )

    with st.expander("**Fitur Utama**"):
        st.write("""
        1. Prediksi Tingkat Kesegaran Buah: Sistem memproses gambar buah dan memberikan estimasi tingkat kesegarannya dalam bentuk persentase.
        2. Rekomendasi Waktu Konsumsi: Berdasarkan tingkat kesegaran, sistem akan merekomendasikan perkiraan waktu terbaik untuk mengonsumsi buah.
        3. Prediksi Penyimpanan: Sistem menyarankan waktu penyimpanan optimal sebelum buah mengalami penurunan kualitas.
        4. Rekomendasi Tempat Penyimpanan: Berdasarkan jenis dan kondisi buah, aplikasi memberikan rekomendasi tempat dan suhu penyimpanan agar buah tetap segar lebih lama.
        
        """)

    with st.expander("**Prasyarat Penggunaan**"):
        st.write("""
        - Gambar buah yang diambil atau diunggah harus terlihat jelas dan memiliki pencahayaan yang cukup agar hasil prediksi akurat.
        - Pastikan aplikasi memiliki akses ke fitur kamera (untuk mengambil foto) atau ke file penyimpanan (untuk mengunggah foto).
        
        """)

    with st.expander("**Langkah Penggunaan**"):
        st.write("""
        1. Buka aplikasi dan pilih tab Konsumen.
        2. Pilih metode pengambilan gambar: Upload foto untuk mengunggah gambar dari galeri atau Ambil foto untuk mengambil gambar langsung menggunakan kamera.
        3. Jika menggunakan Upload foto, pilih gambar dari perangkat Anda. Jika menggunakan Ambil foto, arahkan kamera ke buah, ambil gambar, lalu tekan tombol Simpan Foto untuk menyimpan hasilnya.
        4. Sistem akan menampilkan hasil klasifikasi dan prediksi berupa jenis buah, tingkat kesegaran, rekomendasi waktu konsumsi, prediksi waktu penyimpanan, dan rekomendasi tempat penyimpanan.
        5. Gambar yang diproses beserta hasil analisis akan ditampilkan dalam bentuk card.
        
        """)


    option = st.selectbox("Pilih pengambilan gambar", ["Upload foto", "Ambil foto"])
    images_to_process = []

    if option == "Upload foto":
        uploaded_images = st.file_uploader("Upload gambar buah", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="consumer_upload")
        if uploaded_images:
            images_to_process.extend(uploaded_images)

    elif option == "Ambil foto":
        camera_image = st.camera_input("Ambil gambar dari kamera", key="consumer_camera")
        if camera_image:
            if "captured_images" not in st.session_state:
                st.session_state["captured_images"] = []
            if st.button("Simpan Foto"):
                st.session_state["captured_images"].append(camera_image)
                st.success("Foto berhasil disimpan!")
            images_to_process.extend(st.session_state["captured_images"])

    if images_to_process:
        col1, col2, col3 = st.columns(3)
        columns = [col1, col2, col3]

        for idx, image in enumerate(images_to_process):
            col = columns[idx % 3]
            with col:
                freshness, fruit_type = predict_freshness(image)
                consumption_time, storage_time, storage_recommendation = get_consumer_recommendations(freshness, fruit_type)

                with col.container():
                    # Menggunakan st.image untuk menampilkan gambar secara langsung
                    st.image(image, caption=f"Gambar {idx + 1}", use_column_width=True)

                    # Menampilkan informasi dalam bentuk "card"
                    st.markdown(
                        f"""
                        <div class="card">
                            <h5>Jenis Buah: {fruit_type}</h5>
                            <p>Tingkat Kesegaran: {freshness:.2f}%</p>
                            <h6>Prediksi Konsumsi</h6>
                            <p>Buah dapat dikonsumsi dalam waktu: {consumption_time}</p>
                            <h6>Prediksi Penyimpanan</h6>
                            <p>Buah dapat disimpan hingga: {storage_time}</p>
                            <h6>Rekomendasi Tempat Penyimpanan</h6>
                            <p>{storage_recommendation}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
