import streamlit as st
import  pandas as pd

st.header("_Streamlit_ is :blue[cool] :sunglasses:")

df = pd.read_csv("cars24-car-price.csv")

st.dataframe(df)


agree = st.checkbox("I agree")

if agree:
    st.write("Great!")