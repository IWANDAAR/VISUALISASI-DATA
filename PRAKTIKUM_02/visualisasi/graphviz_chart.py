import streamlit as st 
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("kelompok:21")
st.markdown("""
- Iwanda Aulia Rosando (0110222095)
- Rio Adi Saputro (0110122076) 
- Shila Mumtaz (0110222039)
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""")