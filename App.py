import streamlit as st

#ini adalah Halaman Utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.header('Ini Project Kelompok Sistem Informasi') 

menu = st.sidebar.selectbox('menu', ['Luas persegi', 'Luas Segitiga', 'Luas Lingkaran'])

if menu == 'Luas persegi':
    st.write('ini halaman menghitung luas persegi')
    st.image('luas lingkaran.png',caption='gambar luas persegi')
    def luaspersegi(a):
        return a * a
    sisi = st.number_input('Masukkan sisi persegi', min_value=0,)
    if st.button('Hitung Luas Persegi'):
        luas_persegi = luaspersegi(sisi)
        st.success(f'Luas Persegi adalah: {luas_persegi}')

elif menu == 'Luas Segitiga':
    st.write('ini halaman menghitung luas segitiga')
    st.image('luas segitiga.jpeg',caption='gambar luas segitiga')
    def luassegitiga(a, t):
        return 0.5 * a * t 
    alas = st.number_input('Masukkan alas segitiga', min_value=0,)
    tinggi = st.number_input('Masukkan tinggi segitiga', min_value=0,)
    if st.button('Hitung Luas Segitiga'):
        luas_segitiga = luassegitiga(alas, tinggi)
        st.success(f'Luas Segitiga adalah: {luas_segitiga}')   

elif menu == 'Luas Lingkaran':
    st.write('ini halaman menghitung luas lingkaran')
    st.image('luas lingkaran.jpeg',caption='gambar luas lingkaran')
    def luaslingkaran(r):
        return 3.14 * r * r
    jari_jari = st.number_input('Masukkan jari-jari lingkaran', min_value=0,)
    if st.button('Hitung Luas Lingkaran'):
        luas_lingkaran = luaslingkaran(jari_jari)
        st.success(f'Luas Lingkaran adalah: {luas_lingkaran}')




