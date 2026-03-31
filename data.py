import os
import streamlit as st
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "sales-data.csv")


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load and clean sales data from the CSV file.

    Returns a DataFrame containing only rows with valid (non-null, numeric)
    total_amount values. Displays a warning if any rows were excluded.

    Raises:
        FileNotFoundError: If data/sales-data.csv is missing.
        ValueError: If the file cannot be parsed as a CSV.
    """
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Sales data file not found at '{DATA_PATH}'. "
            "Ensure data/sales-data.csv is present in the repository root."
        )

    try:
        df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    except Exception as e:
        raise ValueError(
            f"Could not read sales data from '{DATA_PATH}'. "
            f"Check that the file is a valid CSV. Details: {e}"
        ) from e

    original_count = len(df)
    df = df[pd.to_numeric(df["total_amount"], errors="coerce").notna()].copy()
    df["total_amount"] = df["total_amount"].astype(float)
    excluded = original_count - len(df)

    if excluded > 0:
        st.warning(
            f"{excluded} row(s) excluded from all calculations due to "
            "missing or non-numeric total_amount values."
        )

    return df


def get_kpis(df: pd.DataFrame) -> dict:
    """Compute top-level KPI values from the cleaned DataFrame.

    Returns:
        dict with keys:
            total_sales (float): Sum of all total_amount values.
            total_orders (int): Count of transaction rows.
    """
    return {
        "total_sales": float(df["total_amount"].sum()),
        "total_orders": int(len(df)),
    }
