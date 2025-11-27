import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.caption("Praktikum 4 - Bar Chart")
st.markdown("""
Kelompok 21
- Iwanda Aulia Rosando (0110222095)
- Rio Adi Saputro (0110122076) 
- Shila Mumtaz (0110222039)
""")


# Data
data = {
    'Jurusan': ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
    'Jumlah Mahasiswa': [120, 150, 100, 80]
}

# Membuat DataFrame Pandas
df = pd.DataFrame(data)

# --- Streamlit App (Cara 1: Menggunakan st.bar_chart) ---
st.title("Basic Bar Chart - Jumlah Mahasiswa per Jurusan")

# st.bar_chart membutuhkan indeks numerik, jadi kolom 'Jurusan' dijadikan indeks.
st.bar_chart(df.set_index('Jurusan'))

# --- Streamlit App (Cara 2: Menggunakan Matplotlib) ---
st.title("Basic Bar Chart Menggunakan Matplotlib")

# Membuat figure dan axes Matplotlib
fig, ax = plt.subplots()

# Membuat bar chart di axes Matplotlib
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menampilkan figure Matplotlib di Streamlit
st.pyplot(fig)
# Asumsi data dari contoh sebelumnya (Perlu didefinisikan di awal file Streamlit Anda)
# data = {
#     'Jurusan': ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
#     'Jumlah Mahasiswa': [120, 150, 100, 80]
# }

st.title("Kustomisasi Basic Bar Chart")

fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'purple']
# Membuat bar chart, dan menyimpannya di variabel 'bars' agar bisa di-iterasi
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menambahkan nilai pada batang
for bar in bars:
    # bar.get_x(): posisi awal batang (kiri)
    # bar.get_width() / 2: digeser ke tengah batang
    # bar.get_height() + 5: nilai di atas batang + sedikit offset
    # str(bar.get_height()): nilai yang ditampilkan
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, str(bar.get_height()), ha='center')

st.pyplot(fig)
st.title("Multiple Basic Bar Chart")

# Data tambahan
data_2023 = [120, 150, 100, 80]
data_2024 = [140, 160, 110, 90]

x = range(len(data['Jurusan']))
width = 0.4

fig, ax = plt.subplots()
# Batang 2023 (posisi x)
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')
# Batang 2024 (posisi x + width)
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Mengatur posisi ticks di tengah kedua batang (x + width / 2)
ax.set_xticks([p + width / 2 for p in x])
# Mengatur label ticks sesuai nama Jurusan
ax.set_xticklabels(data['Jurusan']) 

ax.legend()

st.pyplot(fig)