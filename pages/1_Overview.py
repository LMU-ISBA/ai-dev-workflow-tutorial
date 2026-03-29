import os

import streamlit as st

from src.loader import load_data
from src.transforms import compute_kpis

DATA_PATH = "data/sales-data.csv"

st.title("ShopSmart Sales Dashboard")
st.header("Overview")

try:
    mtime = os.path.getmtime(DATA_PATH)
    df = load_data(DATA_PATH, mtime=mtime)
except (FileNotFoundError, ValueError) as e:
    st.error(str(e))
    st.stop()

kpis = compute_kpis(df)

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Sales", f"${kpis['total_sales']:,.0f}")
with col2:
    st.metric("Total Orders", f"{kpis['total_orders']:,}")
