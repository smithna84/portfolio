import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", use_column_width="auto", caption="Selfie")


with col2:
    st.title("Nathan Smith")
    content = """
    Hi, I am Nathan. I am just starting out in my journey of becoming a Python programmer.
    I want to learn all things Python to not limit myself.
    """

    st.info(content)

content2 = """
Below you can find some apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

data = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")
