import streamlit as st

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu('Turorial Desai Steamlit UTS ML 24/25',
                           ['Klasifikasi', 'Regresi', 'Catatan'],
                           default_index=0)
    
if selected == 'Klasifikasi':
    st.title('Klasifikasi')

    st.write('Untuk Inputan File Dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader("masukan File", type=["csv", "txt"])
    st.write('Untuk usia bisa menggunakan st.slider')
    Age = st.slider("Age",0,100)
    st.write ('Untuk jenis kelamin bisa menggunakan st.radio')
    Sex = st.radio("Gender", ["Female","Male"])
    st.write('Untuk beberapa kolom bisa menggunakan st.selectbox')
    nama_kolom = st.selectbox("Nama Kolom", ["Under","Normal","over"])
    
    st.write('Untuk inputan Manual bisa menggunakan st.number_input')
    panjang = st.number_input("Masukan Nilai Panjang",0)
    lebar = st.number_input("Masukan Nilai Lebar",0)

    jawaban = st.number_input("Masukan Jawaban Anda",min_value=0)
    st.write('Tombol button (menggunakan st.button)')
    hitung = st.button("Prediksi")

    if hitung:
        luas_benar = panjang * lebar
        st.write(f"Panjang : {panjang}, Lebar : {lebar}")
        if jawaban == luas_benar:
            st.success(f"Benar! Luas Persegi Panjang adalah {luas_benar}.")
        else:
            st.error(f"Salah! Luas Persegi Panjang yang benar adalah {luas_benar}.")

if selected == 'Regresi':
    st.title('Regresi')

    st.write('Untuk Inputan File Dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader("masukan File", type=["csv", "txt"])
    st.write('Untuk usia bisa menggunakan st.slider')
    Age = st.slider("Age",0,100)
    st.write ('Untuk jenis kelamin bisa menggunakan st.radio')
    Sex = st.radio("Gender", ["Female","Male"])
    st.write('Untuk beberapa kolom bisa menggunakan st.selectbox')
    nama_kolom = st.selectbox("Nama Kolom", ["Under","Normal","over"])
    
    st.write('Untuk inputan Manual bisa menggunakan st.number_input')
    panjang = st.number_input("Masukan Nilai Panjang",0)
    lebar = st.number_input("Masukan Nilai Lebar",0)
    alas = st.slider("Masukan Nilai Alas",0,100)
    tinggi = st.slider("Masukan Nilai Tinggi",0,100)
    st.write('Tombol button (menggunakan st.button)')
    hitung = st.button("Prediksi")

    if hitung:
        luas =  0.5 * alas * tinggi
        st.write("Luas Segitiga Adalah", luas)

if selected == 'Catatan':
    st.title =('Catatan')
    