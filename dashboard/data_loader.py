"""
Data loading and validation functions for the ShopSmart Sales Dashboard.

This module handles CSV loading, data validation, and aggregation functions
for the dashboard visualizations.
"""

import pandas as pd
import streamlit as st

from dashboard.config import DATA_PATH, REQUIRED_COLUMNS


@st.cache_data
def load_sales_data(file_path: str = DATA_PATH) -> pd.DataFrame:
    """
    Load and validate sales data from a CSV file.

    Args:
        file_path: Path to the CSV file. Defaults to DATA_PATH from config.

    Returns:
        pd.DataFrame: Validated sales data with parsed dates.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If required columns are missing from the CSV.
    """
    # Load CSV with date parsing
    df = pd.read_csv(file_path, parse_dates=["date"])

    # Validate required columns
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Remove duplicate order_ids, keeping first occurrence
    df = df.drop_duplicates(subset=["order_id"], keep="first")

    # Handle missing values in numeric columns
    numeric_columns = ["quantity", "unit_price", "total_amount"]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows with negative amounts
    df = df[df["total_amount"] >= 0]

    return df


def aggregate_sales_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sales data by month for trend visualization.

    Args:
        df: DataFrame with 'date' and 'total_amount' columns.

    Returns:
        pd.DataFrame: Aggregated data with 'month' and 'sales_amount' columns,
                      sorted by month ascending.
    """
    if df.empty:
        return pd.DataFrame(columns=["month", "sales_amount"])

    # Group by month (truncate to first of month)
    df_monthly = df.copy()
    df_monthly["month"] = df_monthly["date"].dt.to_period("M").dt.to_timestamp()

    aggregated = (
        df_monthly.groupby("month")["total_amount"]
        .sum()
        .reset_index()
        .rename(columns={"total_amount": "sales_amount"})
    )

    return aggregated.sort_values("month")


def aggregate_sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sales data by product category.

    Args:
        df: DataFrame with 'category' and 'total_amount' columns.

    Returns:
        pd.DataFrame: Aggregated data with 'category' and 'sales_amount' columns,
                      sorted by sales_amount descending.
    """
    if df.empty:
        return pd.DataFrame(columns=["category", "sales_amount"])

    aggregated = (
        df.groupby("category")["total_amount"]
        .sum()
        .reset_index()
        .rename(columns={"total_amount": "sales_amount"})
    )

    return aggregated.sort_values("sales_amount", ascending=False)


def aggregate_sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sales data by geographic region.

    Args:
        df: DataFrame with 'region' and 'total_amount' columns.

    Returns:
        pd.DataFrame: Aggregated data with 'region' and 'sales_amount' columns,
                      sorted by sales_amount descending.
    """
    if df.empty:
        return pd.DataFrame(columns=["region", "sales_amount"])

    aggregated = (
        df.groupby("region")["total_amount"]
        .sum()
        .reset_index()
        .rename(columns={"total_amount": "sales_amount"})
    )

    return aggregated.sort_values("sales_amount", ascending=False)
