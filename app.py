import streamlit as st
from data import load_data

st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")

st.title("ShopSmart Sales Dashboard")

df = load_data()
