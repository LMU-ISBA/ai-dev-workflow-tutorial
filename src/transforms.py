import pandas as pd


def compute_kpis(df: pd.DataFrame) -> dict:
    """Compute top-level KPI metrics from the sales DataFrame.

    Args:
        df: Validated DataFrame from load_data.

    Returns:
        Dict with keys:
            total_sales (float): Sum of all total_amount values.
            total_orders (int): Count of all rows.
    """
    return {
        "total_sales": float(df["total_amount"].sum()),
        "total_orders": len(df),
    }


def compute_time_series(df: pd.DataFrame, granularity: str) -> pd.DataFrame:
    """Group sales by time period for the trend chart.

    Args:
        df: Validated DataFrame from load_data.
        granularity: "daily" or "monthly".

    Returns:
        DataFrame with columns:
            period (datetime64): Start of the day or month.
            sales (float): Sum of total_amount for that period.
        Sorted ascending by period.

    Raises:
        ValueError: If granularity is not "daily" or "monthly".
    """
    if granularity not in ("daily", "monthly"):
        raise ValueError(
            f"granularity must be 'daily' or 'monthly', got {granularity!r}"
        )

    if granularity == "daily":
        period = df["date"].dt.normalize()
    else:
        period = df["date"].dt.to_period("M").dt.to_timestamp()

    return (
        df.assign(period=period)
        .groupby("period", as_index=False)["total_amount"]
        .sum()
        .rename(columns={"total_amount": "sales"})
        .sort_values("period")
        .reset_index(drop=True)
    )


def compute_category_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by product category.

    Args:
        df: Validated DataFrame from load_data.

    Returns:
        DataFrame with columns:
            category (str): Product category name.
            sales (float): Sum of total_amount for that category.
        Sorted descending by sales.
    """
    return (
        df.groupby("category", as_index=False)["total_amount"]
        .sum()
        .rename(columns={"total_amount": "sales"})
        .sort_values("sales", ascending=False)
        .reset_index(drop=True)
    )


def compute_region_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by geographic region.

    Args:
        df: Validated DataFrame from load_data.

    Returns:
        DataFrame with columns:
            region (str): Geographic region name.
            sales (float): Sum of total_amount for that region.
        Sorted descending by sales.
    """
    return (
        df.groupby("region", as_index=False)["total_amount"]
        .sum()
        .rename(columns={"total_amount": "sales"})
        .sort_values("sales", ascending=False)
        .reset_index(drop=True)
    )
