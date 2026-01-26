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

# Display dashboard content only if data is available
if df is not None:
    # === KPI Section (ECOM-2: T010-T015) ===

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

else:
    st.warning("No data available. Please check the data file.")
