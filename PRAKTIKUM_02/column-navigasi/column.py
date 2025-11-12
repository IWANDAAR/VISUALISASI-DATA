import streamlit as st 

st.title("Columns")
st.write("kelompok:21")
st.markdown("""
- Iwanda Aulia Rosando (0110222095)
- Rio Adi Saputro (0110122076) 
- Shila Mumtaz (0110222039)
""")

coll, col2 = st.columns(2)

coll.write ("ini adalah kolom pertama" )
coll.image ("../../PRAKTIKUM 01/assets/Alexander isak.jpg")
col2.write ("ini adalah kolom kedua")