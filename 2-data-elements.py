import streamlit as st
import pandas as pd #untuk mengelola data dalam bentuk tabel
import numpy as np #untuk membuat data numerik acak 
import altair as alt #untuk membuat chart interactive
import matplotlib.pyplot as plt

st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bagian 2: Data Element")
st.markdown("""
Kelompok 21:
1. Iwanda Aulia Rosando (0110222095)
2. Rio Adi Saputro (0110122076) 
3. Shila Mumtaz (0110222039)
""")

#Dataframe : struktur data berbentuuk table yang memiliki baris dan kolom *diberikan oleh lib pandas
st.subheader("Dataframe")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range (10))
)

#menampilkan dataframe
st.dataframe(df)

#higlight nilai minimum 
st.subheader("Highlight Nilai Minimum")

# highlight nilai terkecil ditiap kolom
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range (10))
)
st.table(df)

#Metrics: komponen tampilan angka penting
st.subheader("Metrics")
st.metric(label="Temperature", value="31 °C", delta="1.2 °C") #kenaikan temperatur
#Metrics sesuai delta_color
#delta color diguanakna utnuk memberikan warna sesuai arah perubahan
# definisikan variable metric
col1, col2, col3 = st.columns(3)
# menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") #naik dan baik
col2.metric(label="Populasi", value="129 Miliyar", delta="1.2 Miliyar", delta_color="inverse") #naik dan buruk
col3.metric(label="Pelanggan", value="100", delta="10", delta_color="off") #netral
# menampilkan metrik temabahan dengan nilai kosong
st.metric(label="Speed", value=None, delta="0") 
st.metric("Trees", "91456", "-1132649")

# menampilkan metrik dengan fungsi write
st.subheader("fungsi write() sebagai superfunction")
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range (10))
)
st.write("here is our data", df, "data is in a dataframe format.\n", "\nwrite is a superfunction")
# fungsi write dengan chart
st.subheader("fungsi write() dengan argument chart")
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)
chart = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b',
    tooltip=['a', 'b']
)
st.write(chart)

# magic 
st.subheader("Magic")
'Adding 6 + 7 = ', 6+7
a = 6,
'a', a
# markdown pakai magic
"""
# ini header
### ini subheader
"""
# dataframe pakai magic
df = pd.DataFrame({'col' : [1,2]})
'### dataframe', df
# chart pakai magic
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
'### chart', chart