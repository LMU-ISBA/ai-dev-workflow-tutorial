"""
ShopSmart Sales Dashboard - Main Application

A Streamlit-based analytics dashboard for visualizing e-commerce sales data.
Displays KPIs, sales trends, and breakdowns by category and region.
"""

import sys
from pathlib import Path

# Add parent directory to path for module imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st

from dashboard.config import PAGE_ICON, PAGE_LAYOUT, PAGE_TITLE
from dashboard.data_loader import (
    aggregate_sales_by_category,
    aggregate_sales_by_month,
    aggregate_sales_by_region,
    load_sales_data,
)
from dashboard.kpi_cards import (
    calculate_total_orders,
    calculate_total_sales,
    format_currency,
    format_number,
)
from dashboard.charts import (
    create_sales_trend_chart,
    create_category_chart,
    create_region_chart,
)


def render_kpi_section(df) -> None:
    """Render the KPI cards section at the top of the dashboard."""
    total_sales = calculate_total_sales(df)
    total_orders = calculate_total_orders(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Total Sales",
            value=format_currency(total_sales),
        )

    with col2:
        st.metric(
            label="Total Orders",
            value=format_number(total_orders),
        )


def render_dashboard() -> None:
    """Main function that assembles and renders all dashboard components."""
    # Page configuration - must be first Streamlit command
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=PAGE_LAYOUT,
    )

    # Dashboard title
    st.title("📊 ShopSmart Sales Dashboard")

    # Load data with error handling
    try:
        df = load_sales_data()
    except FileNotFoundError:
        st.error("❌ Data file not found. Please ensure 'data/sales-data.csv' exists.")
        return
    except ValueError as e:
        st.error(f"❌ Data validation error: {e}")
        return

    # Handle empty data
    if df.empty:
        st.warning("⚠️ No data available. The data file appears to be empty.")
        render_kpi_section(df)
        return

    # Render KPI section
    st.markdown("---")
    render_kpi_section(df)

    # Sales Trend Chart
    st.markdown("---")
    monthly_data = aggregate_sales_by_month(df)
    if not monthly_data.empty:
        trend_chart = create_sales_trend_chart(monthly_data)
        st.plotly_chart(trend_chart, use_container_width=True)
    else:
        st.info("📈 No trend data available.")

    # Category and Region Charts (side by side)
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        category_data = aggregate_sales_by_category(df)
        if not category_data.empty:
            category_chart = create_category_chart(category_data)
            st.plotly_chart(category_chart, use_container_width=True)
        else:
            st.info("📊 No category data available.")

    with col2:
        region_data = aggregate_sales_by_region(df)
        if not region_data.empty:
            region_chart = create_region_chart(region_data)
            st.plotly_chart(region_chart, use_container_width=True)
        else:
            st.info("🗺️ No region data available.")


if __name__ == "__main__":
    render_dashboard()
