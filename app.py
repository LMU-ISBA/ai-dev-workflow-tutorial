import streamlit as st
from data import load_data, get_kpis

st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")

st.title("ShopSmart Sales Dashboard")

df = load_data()

# --- KPI Scorecards ---
kpis = get_kpis(df)
col1, col2 = st.columns(2)
col1.metric(label="Total Sales", value=f"${kpis['total_sales']:,.0f}")
col2.metric(label="Total Orders", value=f"{kpis['total_orders']:,}")
