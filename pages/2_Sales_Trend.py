import os

import plotly.express as px
import streamlit as st

from src.loader import load_data
from src.transforms import compute_time_series

DATA_PATH = "data/sales-data.csv"

st.header("Sales Trend")

try:
    mtime = os.path.getmtime(DATA_PATH)
    df = load_data(DATA_PATH, mtime=mtime)
except (FileNotFoundError, ValueError) as e:
    st.error(str(e))
    st.stop()

granularity_label = st.radio("Granularity", ["Monthly", "Daily"], index=0)
granularity = "monthly" if granularity_label == "Monthly" else "daily"

ts = compute_time_series(df, granularity)
fig = px.line(ts, x="period", y="sales", title="Sales Trend")
st.plotly_chart(fig, use_container_width=True)
