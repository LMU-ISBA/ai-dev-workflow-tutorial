import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ShopSmart Sales Dashboard", page_icon="📊", layout="wide"
)

st.title("ShopSmart Sales Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("data/sales-data.csv", parse_dates=["date"])
    return df


df = load_data()

total_sales = df["total_amount"].sum()
total_orders = df["order_id"].nunique()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")

st.markdown("---")

monthly_sales = df.set_index("date").resample("ME")["total_amount"].sum().reset_index()
monthly_sales.columns = ["Month", "Sales"]

fig_trend = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    title="Sales Trend Over Time",
    labels={"Sales": "Sales ($)", "Month": "Month"},
)
fig_trend.update_layout(hovermode="x unified")
st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("---")

left, right = st.columns(2)

with left:
    category_sales = (
        df.groupby("category")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    category_sales.columns = ["Category", "Sales"]
    fig_cat = px.bar(
        category_sales,
        x="Sales",
        y="Category",
        orientation="h",
        title="Sales by Category",
        labels={"Sales": "Sales ($)"},
    )
    fig_cat.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_cat, use_container_width=True)

with right:
    region_sales = (
        df.groupby("region")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    region_sales.columns = ["Region", "Sales"]
    fig_reg = px.bar(
        region_sales,
        x="Sales",
        y="Region",
        orientation="h",
        title="Sales by Region",
        labels={"Sales": "Sales ($)"},
    )
    fig_reg.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_reg, use_container_width=True)
