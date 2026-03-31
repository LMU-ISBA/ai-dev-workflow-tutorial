import streamlit as st
import plotly.express as px
from data import load_data, get_kpis, get_monthly_trend

st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")

st.title("ShopSmart Sales Dashboard")

df = load_data()

# --- KPI Scorecards ---
kpis = get_kpis(df)
col1, col2 = st.columns(2)
col1.metric(label="Total Sales", value=f"${kpis['total_sales']:,.0f}")
col2.metric(label="Total Orders", value=f"{kpis['total_orders']:,}")

# --- Sales Trend Chart ---
trend = get_monthly_trend(df)
fig_trend = px.line(
    trend,
    x="month",
    y="sales",
    title="Sales Trend",
    labels={"month": "Month", "sales": "Sales ($)"},
)
st.plotly_chart(fig_trend, use_container_width=True)
