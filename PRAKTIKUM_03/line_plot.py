import streamlit as st 

import matplotlib.pyplot as plt 

months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Des']
product_a_sales = [56, 78.90, 43, 45, 67, 12, 48, 80, 12, 24, 50, 90] 
product_b_sales = [66, 71.35, 36, 48, 70, 24, 34, 90, 98, 1, 30, 90] 

st.title("Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot", "Multiple & Customization", "Jenis Garis Untuk Menunjukkan Tren", "Subplot"))

st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
Kelompok 21
- Iwanda Aulia Rosando (0110222095)
- Rio Adi Saputro (0110122076) 
- Shila Mumtaz (0110222039)
""")

def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_a_sales, label="Produk A")
    ax.set_title('Penjualan Produk A Perbulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.grid(True)
    st.pyplot(fig)

def multiple_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_a_sales, label="Produk A", marker="o", linestyle="--")
    ax.plot(months, product_b_sales, label="Produk B", marker="x", linestyle="-")

    ax.set_title('Penjualan Produk Perbulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


product_c_sales=[56, 24, 67, 45, 24, 10, 90, 78, 56, 34, 23, 45]
product_d_sales=[67, 34, 78, 23, 45, 66, 77, 12, 34, 56, 89, 99]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_c_sales, label="Produk C", color='green', linestyle="dashdot")
    axs.plot(months, product_d_sales, label="Produk D", color='purple', linestyle=":")
    axs.set_title('Penjualan Produk A (Jenis Garis)')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.grid(axis='y', linestyle=':')
    st.pyplot(fig)

def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    axs[0].plot(months, product_c_sales, label="Produk C", linestyle="--")
    axs[0].set_title('Produk Penjualan Produk C Perbulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Penjualan')
    axs[0].legend()
    axs[0].grid('true')

    axs[1].plot(months, product_d_sales, label="Produk D", linestyle="--")
    axs[1].set_title('Produk Penjualan Produk D Perbulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Penjualan')
    axs[1].legend()
    axs[1].grid('true')

    plt.tight_layout()
    st.pyplot(fig)
 
if option == "Single Line Plot" :
    line_plot()
elif option == "Multiple & Customization" :
    multiple_line_plot() 
elif option == "Jenis Garis Untuk Menunjukkan Tren" :
    tren_line_plot()
elif option == "Subplot" :
    subplots()