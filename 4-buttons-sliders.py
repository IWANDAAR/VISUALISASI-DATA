import streamlit as st
import time 

st.header("Praktikum 4 Button & Sliders")
st.subheader("Bagian 4: Button & Sliders")
st.markdown("""
Kelompok 21:
1. Iwanda Aulia Rosando (0110222095)
2. Rio Adi Saputro (0110122076) 
3. Shila Mumtaz (0110222039)
""")

# membuat tombol biasa
st.header("Buat Tombol")
tombol = st.button("Klik Saya")
if tombol:
    st.write("Sudah  klik")
else :
    st.write("Belum klik")

# membuat tombol radio
st.header("Buat Tombol Radio")
team = st.radio("Pilih karakter", ("bambang", "yanto", "budi", "agus"))

if team == "liverpool":
    st.write("Anda fans liverpool")
elif team == "chelsea":
    st.write("Anda fans chelsea")
elif team == "PERSIJA":
    st.write("Anda fans persija")
elif team == "PSMS MEDAN":
    st.write("Anda fans PSMS MEDAN")
else:
    st.write("Anda bukan fans PSMS MEDAN")

# membuat tombol check
st.header("Buat Tombol Check")
st.write("Pilihlah yang anda suka")
hobi = st.checkbox("Futsal")
hobi2 = st.checkbox("Bulu Tangkis")
hobi3 = st.checkbox("Sepak Bola")

# membuat tombol dropdown
st.header("Buat Tombol Dropdown")
team = st.selectbox("Pilih karakter", ("bambang", "yanto", "budi", "agus"))

# membuat tombol multi pilihan 
st.header("Buat Tombol Multi Pilihan")
team = st.multiselect("Pilih karakter", ("bambang", "yanto", "budi", "agus"))

# membuat tombol download 
st.header("Buat Tombol Download")
downLoad = st.download_button(
label = "Download Gambar",
data =open("assets\silverstone.jpg", "rb"),
file_name = "silverstone.jpg",
mime = "image/jpg"
)

# membuat tampilan batang progress
st.header("Progress  Sekarang")
progres = st.progress(0)
for i in range(100):
    time.sleep(0.2)
    progres.progress(i+1)
st.write("Selesai")

# membuat tampilan spinner
st.header("Spinner Sekarang")
with st.spinner("Loading...."):
    time.sleep(10)
st.write("Selesai")