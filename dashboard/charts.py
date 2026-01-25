"""
Chart creation functions for the ShopSmart Sales Dashboard.

This module provides Plotly chart generation functions for sales visualizations.
All charts are interactive with hover tooltips per FR-006.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dashboard.config import COLOR_SEQUENCE


def create_sales_trend_chart(df: pd.DataFrame) -> go.Figure:
    """
    Create a line chart showing sales trends over time.

    Args:
        df: DataFrame with 'month' and 'sales_amount' columns
            (from aggregate_sales_by_month).

    Returns:
        plotly.graph_objects.Figure: Interactive line chart.
    """
    fig = px.line(
        df,
        x="month",
        y="sales_amount",
        title="Sales Trend Over Time",
        labels={
            "month": "Month",
            "sales_amount": "Sales Amount",
        },
        color_discrete_sequence=COLOR_SEQUENCE,
    )

    # Configure hover template with currency formatting
    fig.update_traces(
        hovertemplate="<b>%{x|%B %Y}</b><br>Sales: $%{y:,.2f}<extra></extra>",
        line=dict(width=3),
        mode="lines+markers",
    )

    # Configure layout for professional appearance
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales Amount ($)",
        yaxis_tickformat="$,.0f",
        hovermode="x unified",
        showlegend=False,
    )

    return fig


def create_category_chart(df: pd.DataFrame) -> go.Figure:
    """
    Create a horizontal bar chart showing sales by category.

    Args:
        df: DataFrame with 'category' and 'sales_amount' columns
            (from aggregate_sales_by_category).

    Returns:
        plotly.graph_objects.Figure: Interactive horizontal bar chart.
    """
    # Sort ascending so highest appears at top in horizontal bar
    df_sorted = df.sort_values("sales_amount", ascending=True)

    fig = px.bar(
        df_sorted,
        x="sales_amount",
        y="category",
        orientation="h",
        title="Sales by Category",
        labels={
            "category": "Category",
            "sales_amount": "Sales Amount",
        },
        color_discrete_sequence=COLOR_SEQUENCE,
    )

    # Configure hover template
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>",
    )

    # Configure layout
    fig.update_layout(
        xaxis_title="Sales Amount ($)",
        yaxis_title="",
        xaxis_tickformat="$,.0f",
        showlegend=False,
    )

    return fig


def create_region_chart(df: pd.DataFrame) -> go.Figure:
    """
    Create a horizontal bar chart showing sales by region.

    Args:
        df: DataFrame with 'region' and 'sales_amount' columns
            (from aggregate_sales_by_region).

    Returns:
        plotly.graph_objects.Figure: Interactive horizontal bar chart.
    """
    # Sort ascending so highest appears at top in horizontal bar
    df_sorted = df.sort_values("sales_amount", ascending=True)

    fig = px.bar(
        df_sorted,
        x="sales_amount",
        y="region",
        orientation="h",
        title="Sales by Region",
        labels={
            "region": "Region",
            "sales_amount": "Sales Amount",
        },
        color_discrete_sequence=[COLOR_SEQUENCE[1]],  # Use different color
    )

    # Configure hover template
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>",
    )

    # Configure layout
    fig.update_layout(
        xaxis_title="Sales Amount ($)",
        yaxis_title="",
        xaxis_tickformat="$,.0f",
        showlegend=False,
    )

    return fig
