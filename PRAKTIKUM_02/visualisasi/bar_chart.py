import streamlit as st 
import pandas as pd
import numpy as np

st.title("Bar Chart")
st.write("kelompok:21")
st.markdown("""
- Iwanda Aulia Rosando (0110222095)
- Rio Adi Saputro (0110122076) 
- Shila Mumtaz (0110222039)
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns= ["C1", "C2", "C3", "C4"]
)

st.bar_chart(df)
