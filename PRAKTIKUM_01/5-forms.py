import streamlit as st
import datetime 
import pandas as pd 

st.header("Praktikum 5 Forms")
st.subheader("Bagian 5: membuat banyak tipe form")
st.markdown("""
Kelompok 21:
1. Iwanda Aulia Rosando (0110222095)
2. Rio Adi Saputro (0110122076) 
3. Shila Mumtaz (0110222039)
""")

# membuat textbox
st.header("Buat Textbox")
NamaLengkap = st.text_input("Masukkan Nama Lengkap Anda")
st.write("Nama Lengkap Anda Adalah: ",NamaLengkap)
# membuat textbox tipe password
st.header("Buat Textbox Tipe Password")
Password = st.text_input("Masukkan Password Anda", type="password")
# membuat textbox maksimal 5 karakter
st.header("Buat Textbox Maksimal 5 Karakter")
NamaLengkap = st.text_input("Masukkan Nama Lengkap Anda", max_chars=5)

# membuat text area
TeksArea = st.text_area("Masukkan Teks Anda")
st.write("Teks Anda Adalah: ",TeksArea)

# membuat form pengisian angka
st.header("Buat Form Pengisian Angka")
st.write("minimal angka adalah 0, \n maksimal angka adalah 1000")
AngkA = st.number_input("Masukkan angka", min_value=0, max_value=1000, value=5, step=10)
st.write("default angka adalah 5, \n step angka adalah 10")
st.write("Total Nilai Angka Anda Adalah: ",AngkA)

# membuat form input waktu
st.header("Buat Form Input Waktu")
st.time_input("Masukkan waktu lokal anda")

# membuat form input tanggal
st.header("Buat Form Input Tanggal")
st.date_input("Pilih Tanggal Mu", value=datetime.date(2025, 11, 2),
min_value=datetime.date(2025, 11, 2),
max_value=datetime.date(2100, 1, 1))

# membuat form input warna
st.header("Buat Form Input Warna")
warna = st.color_picker("Pilih Warna")
st.write("Warna Anda Adalah: ",warna)

# membuat form up dataset
st.header("Buat Form Upload Dataset")
file = st.file_uploader("Upload Dataset",type=["csv"])
detail = st.button("Detail Dataset")
if detail :
    if file is not None:
        detail_data_file = {"nama file":file.name, "tipe file":file.type, "ukuran file":file.size}
        st.write("Detail File:")
        st.write(detail_data_file)
        st.write("Preview Dataset:")
        df = pd.read_csv(file)
        st.dataframe(df)
    else:
        st.write("Tidak ada file yang diupload") 

# membuat tombol kirim untuk form
form = st.form(key="my-form")
a = form.text_input(label='Masukkan Nama Anda')
button = form.form_submit_button(label='Kirim')
st.write("Nama Anda Adalah: ",a)