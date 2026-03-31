"""
KPI calculation and formatting functions for the ShopSmart Sales Dashboard.

This module provides functions to calculate key performance indicators
and format them for display.
"""

import pandas as pd

from dashboard.config import CURRENCY_FORMAT, NUMBER_FORMAT


def calculate_total_sales(df: pd.DataFrame) -> float:
    """
    Calculate the total sales amount from the sales data.

    Args:
        df: DataFrame with 'total_amount' column.

    Returns:
        float: Sum of all total_amount values. Returns 0.0 if DataFrame is empty.
    """
    if df.empty:
        return 0.0

    return df["total_amount"].sum()


def calculate_total_orders(df: pd.DataFrame) -> int:
    """
    Count the total number of unique orders.

    Args:
        df: DataFrame with 'order_id' column.

    Returns:
        int: Count of unique order_id values. Returns 0 if DataFrame is empty.
    """
    if df.empty:
        return 0

    return df["order_id"].nunique()


def format_currency(value: float) -> str:
    """
    Format a numeric value as US currency.

    Args:
        value: Numeric value to format.

    Returns:
        str: Formatted string as "$X,XXX,XXX.XX"
    """
    return CURRENCY_FORMAT.format(value)


def format_number(value: int) -> str:
    """
    Format an integer with thousand separators.

    Args:
        value: Integer value to format.

    Returns:
        str: Formatted string with commas as thousand separators.
    """
    return NUMBER_FORMAT.format(value)
