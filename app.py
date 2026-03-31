import streamlit as st
import plotly.express as px
from data import load_data, get_kpis, get_monthly_trend, get_category_breakdown, get_region_breakdown

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

# --- Category & Region Bar Charts ---
col3, col4 = st.columns(2)

with col3:
    cat = get_category_breakdown(df)
    fig_cat = px.bar(
        cat,
        x="category",
        y="sales",
        title="Sales by Category",
        labels={"category": "Category", "sales": "Sales ($)"},
    )
    st.plotly_chart(fig_cat, use_container_width=True)

with col4:
    reg = get_region_breakdown(df)
    fig_reg = px.bar(
        reg,
        x="region",
        y="sales",
        title="Sales by Region",
        labels={"region": "Region", "sales": "Sales ($)"},
    )
    st.plotly_chart(fig_reg, use_container_width=True)
