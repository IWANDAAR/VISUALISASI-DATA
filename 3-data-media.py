import streamlit as st 
import base64
from PIL import Image

st.header("Praktikum 3 Visualisasi Data")
st.subheader("Bagian 3: Data Media")
st.markdown("""
Kelompok 21:
1. Iwanda Aulia Rosando (0110222095)
2. Rio Adi Saputro (0110122076) 
3. Shila Mumtaz (0110222039)
""")

# menampilkan gambar biasa
st.write(" Mempersembahkan Gambar king Liverpool")
st.image("assets\IMG_7933-724x1024.webp")
st.write("Sumber Image: Ambisius wiki")
# menampilkan multiple gambar
st.write("Mempersembahkan sang mega bintang Liverpool")
w15 = [
    "assets\Alexander isak.jpg",
    "assets\Alexis Mcalisterr.webp",
    "assets\Dominic szoboslai.jpg",
]
st.image(w15, width=230)
st.write("Sumber Image: Google")


# backgound image
def background_image(gambar):
    with open(gambar, "rb") as gambar:
        encoded_string = base64.b64encode(gambar.read())
    st.write("Sumber Image: Google")
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }},
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Menampilkan Background Image")
background_image("assets\mercedes-dark.jpg")


# mengubah ukuran gambar 
gambar_ori = Image.open("assets\w11-in-barcelona.jpg")
st.title("Gambar Asli")
st.image(gambar_ori)
ubah_ukuran = gambar_ori.resize((400, 300))
st.title("Gambar Resized")
st.image(ubah_ukuran)