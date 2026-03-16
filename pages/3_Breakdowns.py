import os

import plotly.express as px
import streamlit as st

from src.loader import load_data
from src.transforms import compute_category_sales, compute_region_sales

DATA_PATH = "data/sales-data.csv"

st.header("Breakdowns")

try:
    mtime = os.path.getmtime(DATA_PATH)
    df = load_data(DATA_PATH, mtime=mtime)
except (FileNotFoundError, ValueError) as e:
    st.error(str(e))
    st.stop()

cat_df = compute_category_sales(df)
fig_cat = px.bar(cat_df, x="category", y="sales", title="Sales by Category")
st.plotly_chart(fig_cat, use_container_width=True)

reg_df = compute_region_sales(df)
fig_reg = px.bar(reg_df, x="region", y="sales", title="Sales by Region")
st.plotly_chart(fig_reg, use_container_width=True)
