import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


st.caption("Praktikum 4 - Pola dan trend")
st.markdown("""
Kelompok 21
- Iwanda Aulia Rosando (0110222095)
- Rio Adi Saputro (0110122076) 
- Shila Mumtaz (0110222039)
""")

# Data jumlah mahasiswa per jurusan selama 5 tahun
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

# Membuat dataframe untuk visualisasi
df = pd.DataFrame(data)

# --- Streamlit App ---
st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

# Menambahkan filter tahun
filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

# Menambahkan filter jurusan
jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)

# --- Filter Data ---
# Memfilter baris (Tahun)
# Membuat list kolom yang akan ditampilkan: ['Tahun'] + daftar jurusan yang difilter
kolom_tampil = ['Tahun'] + filter_jurusan

# df['Tahun'].isin(filter_tahun) menghasilkan array boolean (True/False)
# df[...][kolom_tampil] memilih baris yang True dan kolom yang dipilih
filtered_data = df[df['Tahun'].isin(filter_tahun)][kolom_tampil]

# --- Menampilkan Data Tabel ---
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# --- Membuat Bar Chart dengan Filter ---
st.subheader("Bar Chart dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat Bar Chart berdasarkan data yang difilter
x = range(len(filtered_data['Tahun'])) # Posisi batang berdasarkan jumlah tahun yang dipilih
width = 0.2

# Loop untuk membuat batang ganda (grouped bar chart)
for i, jur in enumerate(filter_jurusan):
    # Batang digeser i * width untuk setiap jurusan
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

# Menyesuaikan sumbu dan judul
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")

# Mengatur posisi ticks X di tengah kelompok batang
# width * len(filter_jurusan) / 2: Titik tengah total lebar kelompok batang
# - width / 2: penyesuaian untuk Matplotlib
posisi_tick = [p + width * len(filter_jurusan) / 2 - width / 2 for p in x]
ax.set_xticks(posisi_tick)
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

# Menampilkan plot di Streamlit
st.pyplot(fig)