import streamlit as st
from streamlit_option_menu import option_menu
from utility import consumer, farmer, about

# Konfigurasi awal
st.set_page_config(page_title="Freshty.id", 
                   page_icon='🍊',
                   layout="wide",
                   )

# Tambahkan CSS untuk styling
st.markdown(
    """
    <style>

    /* Atur margin dan padding untuk tampilan utama */
    .main-container {
        padding-left: 5rem;
        padding-right: 5rem;
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: #EEDF7A;
    }

    /* Styling untuk header dan teks utama */
    h1, h2, h3, h4, h5, h6 {
        color: #EEDF7A;
    }
    .stApp {
        background-color: #;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Pengaturan menu utama
selected_tab = option_menu(
    menu_title=None,
    options=["About Us", "Konsumen", "Petani"],
    icons=["info-circle", "person", "people"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Atur padding horizontal menggunakan kolom kosong di kiri dan kanan
col1, main_col, col3 = st.columns([0.2, 1.3, 0.2])  # Sesuaikan rasio sesuai kebutuhan
with col1:
    st.write("")  # Kosong sebagai padding kiri

with main_col:
    # Konten utama disini
    if selected_tab == "About Us":
        about.show_about_page()
    elif selected_tab == "Konsumen":
        consumer.show_consumer_page()
    elif selected_tab == "Petani":
        farmer.show_farmer_page()

with col3:
    st.write("")  # Kosong sebagai padding kanan
