import os

import pandas as pd
import streamlit as st

REQUIRED_COLUMNS = {
    "date",
    "order_id",
    "product",
    "category",
    "region",
    "quantity",
    "unit_price",
    "total_amount",
}


@st.cache_data
def load_data(path: str, mtime: float) -> pd.DataFrame:
    """Load and validate the sales CSV.

    The mtime parameter is included in Streamlit's cache key so the cache
    busts automatically whenever the file changes on disk.

    Args:
        path: Path to the CSV file.
        mtime: File modification timestamp from os.path.getmtime(path).

    Returns:
        Validated DataFrame with columns: date, order_id, product, category,
        region, quantity, unit_price, total_amount.

    Raises:
        FileNotFoundError: If the file does not exist at path.
        ValueError: If required columns are missing or total_amount is non-numeric.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Data file error: file not found\n"
            f"Expected file: {path}\n"
            f"Ensure the file exists at the expected path and try again."
        )

    try:
        df = pd.read_csv(path, parse_dates=["date"])
    except Exception as e:
        raise ValueError(
            f"Data file error: could not read CSV — {e}\n"
            f"Expected file: {path}\n"
            f"Ensure the file is a valid CSV and try again."
        ) from e

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(
            f"Data file error: missing required columns: {sorted(missing)}\n"
            f"Expected file: {path}\n"
            f"Add the missing columns to the CSV and try again."
        )

    if not pd.api.types.is_numeric_dtype(df["total_amount"]):
        raise ValueError(
            f"Data file error: 'total_amount' column must be numeric\n"
            f"Expected file: {path}\n"
            f"Ensure all values in 'total_amount' are numbers and try again."
        )

    return df
