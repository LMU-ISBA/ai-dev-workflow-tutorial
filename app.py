"""
ShopSmart Sales Dashboard

An interactive analytics dashboard for e-commerce sales data.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# Page configuration
st.set_page_config(
    page_title="ShopSmart Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Main title
st.title("ShopSmart Sales Dashboard")


# Data loading function with caching for performance (T005, T006, T007, T008)
@st.cache_data
def load_data() -> pd.DataFrame | None:
    """
    Load sales data from CSV file.

    Returns:
        DataFrame with sales data, or None if loading fails.
    """
    data_path = Path("data/sales-data.csv")

    try:
        # Load CSV with date parsing
        df = pd.read_csv(data_path, parse_dates=["date"])

        # Validate: check if DataFrame is empty
        if df.empty:
            return None

        return df

    except FileNotFoundError:
        st.error(f"Data file not found: {data_path}")
        st.info("Please ensure 'data/sales-data.csv' exists in the project directory.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None


# Load the data
df = load_data()

# T038: Consistent color scheme for all charts
COLOR_SCHEME = "#1f77b4"  # Plotly default blue

# Display dashboard content only if data is available
if df is not None:
    # === KPI Section (ECOM-2: T010-T015) ===
    # T039: Section header
    st.subheader("Key Performance Indicators")

    # T010: Calculate total sales
    total_sales = df["total_amount"].sum()

    # T011: Calculate total orders
    total_orders = df["order_id"].count()

    # T012: Create KPI display with two columns
    kpi_col1, kpi_col2 = st.columns(2)

    # T013: Display Total Sales with currency formatting
    with kpi_col1:
        st.metric(
            label="Total Sales",
            value=f"${total_sales:,.2f}"
        )

    # T014: Display Total Orders with number formatting
    with kpi_col2:
        st.metric(
            label="Total Orders",
            value=f"{total_orders:,}"
        )

    # T039: Section divider
    st.divider()

    # === Sales Trend Section (ECOM-3: T016-T023) ===
    st.subheader("Sales Trends")

    # T016, T017: Create monthly sales aggregation
    df["month"] = df["date"].dt.to_period("M")
    monthly_sales = df.groupby("month")["total_amount"].sum().reset_index()
    monthly_sales["month"] = monthly_sales["month"].dt.to_timestamp()

    # T018-T022: Create Plotly line chart with consistent color
    fig_trend = px.line(
        monthly_sales,
        x="month",
        y="total_amount",
        title="Sales Trend Over Time",
        labels={"month": "Month", "total_amount": "Sales Amount ($)"}
    )

    # T019, T020: Configure axes formatting
    fig_trend.update_xaxes(tickformat="%b %Y")
    fig_trend.update_yaxes(tickprefix="$", tickformat=",.0f")

    # T021: Interactive tooltips
    fig_trend.update_traces(
        hovertemplate="<b>%{x|%B %Y}</b><br>Sales: $%{y:,.2f}<extra></extra>",
        line_color=COLOR_SCHEME
    )

    # T023: Display chart with full container width
    st.plotly_chart(fig_trend, use_container_width=True)

    # T039: Section divider
    st.divider()

    # === Sales Breakdown Section (ECOM-4, ECOM-5) ===
    st.subheader("Sales Breakdown")

    # T037: Arrange Category and Region charts side-by-side
    chart_col1, chart_col2 = st.columns(2)

    # === Sales by Category (ECOM-4: T024-T029) ===
    with chart_col1:
        # T024: Create category sales aggregation
        category_sales = df.groupby("category")["total_amount"].sum().reset_index()

        # T025: Sort by total sales descending
        category_sales = category_sales.sort_values("total_amount", ascending=True)

        # T026, T027, T029: Create Plotly horizontal bar chart with consistent color
        fig_category = px.bar(
            category_sales,
            x="total_amount",
            y="category",
            orientation="h",
            title="Sales by Product Category",
            labels={"total_amount": "Sales Amount ($)", "category": "Category"}
        )

        # T028: Add interactive tooltips
        fig_category.update_traces(
            hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>",
            marker_color=COLOR_SCHEME
        )

        # Configure axis formatting
        fig_category.update_xaxes(tickprefix="$", tickformat=",.0f")

        st.plotly_chart(fig_category, use_container_width=True)

    # === Sales by Region (ECOM-5: T030-T035) ===
    with chart_col2:
        # T030: Create region sales aggregation
        region_sales = df.groupby("region")["total_amount"].sum().reset_index()

        # T031: Sort by total sales descending
        region_sales = region_sales.sort_values("total_amount", ascending=True)

        # T032, T033, T035: Create Plotly horizontal bar chart with consistent color
        fig_region = px.bar(
            region_sales,
            x="total_amount",
            y="region",
            orientation="h",
            title="Sales by Region",
            labels={"total_amount": "Sales Amount ($)", "region": "Region"}
        )

        # T034: Add interactive tooltips
        fig_region.update_traces(
            hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>",
            marker_color=COLOR_SCHEME
        )

        # Configure axis formatting
        fig_region.update_xaxes(tickprefix="$", tickformat=",.0f")

        st.plotly_chart(fig_region, use_container_width=True)

else:
    # T040: Edge case - empty data shows appropriate message
    st.warning("No data available. Please check the data file.")
