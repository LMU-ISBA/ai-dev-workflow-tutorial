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


def get_monthly_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total_amount by calendar month.

    Returns:
        DataFrame with columns ["month" (str, "YYYY-MM"), "sales" (float)],
        12 rows sorted ascending. Months with no transactions are zero-filled.
    """
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M").astype(str)
    monthly = df.groupby("month", as_index=False)["total_amount"].sum()
    monthly = monthly.rename(columns={"total_amount": "sales"})

    # Ensure all 12 months of 2024 are present
    all_months = [f"2024-{m:02d}" for m in range(1, 13)]
    full = pd.DataFrame({"month": all_months})
    monthly = full.merge(monthly, on="month", how="left").fillna(0)
    monthly["sales"] = monthly["sales"].astype(float)
    return monthly.sort_values("month").reset_index(drop=True)


KNOWN_CATEGORIES = ["Electronics", "Accessories", "Audio", "Wearables", "Smart Home"]
KNOWN_REGIONS = ["North", "South", "East", "West"]


def get_category_breakdown(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total_amount by product category.

    Returns:
        DataFrame with columns ["category", "sales"], all 5 known categories
        present, sorted descending by sales.
    """
    breakdown = df.groupby("category", as_index=False)["total_amount"].sum()
    breakdown = breakdown.rename(columns={"total_amount": "sales"})
    full = pd.DataFrame({"category": KNOWN_CATEGORIES})
    breakdown = full.merge(breakdown, on="category", how="left").fillna(0)
    breakdown["sales"] = breakdown["sales"].astype(float)
    return breakdown.sort_values("sales", ascending=False).reset_index(drop=True)


def get_region_breakdown(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total_amount by geographic region.

    Returns:
        DataFrame with columns ["region", "sales"], all 4 known regions
        present, sorted descending by sales.
    """
    breakdown = df.groupby("region", as_index=False)["total_amount"].sum()
    breakdown = breakdown.rename(columns={"total_amount": "sales"})
    full = pd.DataFrame({"region": KNOWN_REGIONS})
    breakdown = full.merge(breakdown, on="region", how="left").fillna(0)
    breakdown["sales"] = breakdown["sales"].astype(float)
    return breakdown.sort_values("sales", ascending=False).reset_index(drop=True)


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
