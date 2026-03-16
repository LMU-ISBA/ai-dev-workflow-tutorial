import pandas as pd
import pytest

from src.transforms import compute_kpis, compute_time_series, compute_category_sales, compute_region_sales


def make_df():
    return pd.DataFrame({
        "date": pd.to_datetime(["2024-01-01", "2024-01-15", "2024-02-01"]),
        "order_id": ["ORD-001", "ORD-002", "ORD-003"],
        "product": ["Widget A", "Widget B", "Widget C"],
        "category": ["Electronics", "Audio", "Electronics"],
        "region": ["North", "South", "North"],
        "quantity": [1, 2, 3],
        "unit_price": [100.0, 50.0, 25.0],
        "total_amount": [100.0, 100.0, 75.0],
    })


class TestComputeKpis:
    def test_total_sales(self):
        result = compute_kpis(make_df())
        assert result["total_sales"] == 275.0

    def test_total_orders(self):
        result = compute_kpis(make_df())
        assert result["total_orders"] == 3

    def test_total_sales_is_float(self):
        result = compute_kpis(make_df())
        assert isinstance(result["total_sales"], float)

    def test_empty_dataframe_returns_zeros(self):
        empty = pd.DataFrame({"total_amount": pd.Series([], dtype=float)})
        result = compute_kpis(empty)
        assert result["total_sales"] == 0.0
        assert result["total_orders"] == 0


class TestComputeTimeSeries:
    def test_monthly_produces_one_row_per_month(self):
        ts = compute_time_series(make_df(), "monthly")
        assert len(ts) == 2  # Jan and Feb

    def test_daily_produces_one_row_per_day(self):
        ts = compute_time_series(make_df(), "daily")
        assert len(ts) == 3  # Jan 1, Jan 15, Feb 1

    def test_output_sorted_ascending_by_period(self):
        ts = compute_time_series(make_df(), "monthly")
        assert list(ts["period"]) == sorted(ts["period"].tolist())

    def test_monthly_sales_aggregated_correctly(self):
        ts = compute_time_series(make_df(), "monthly")
        jan = ts[ts["period"].dt.month == 1].iloc[0]["sales"]
        assert jan == 200.0  # 100 + 100

    def test_invalid_granularity_raises_value_error(self):
        with pytest.raises(ValueError, match="granularity"):
            compute_time_series(make_df(), "weekly")

    def test_output_columns(self):
        ts = compute_time_series(make_df(), "daily")
        assert list(ts.columns) == ["period", "sales"]


class TestComputeCategorySales:
    def test_sorted_descending(self):
        result = compute_category_sales(make_df())
        assert result["sales"].is_monotonic_decreasing

    def test_all_categories_present(self):
        result = compute_category_sales(make_df())
        assert set(result["category"]) == {"Electronics", "Audio"}

    def test_aggregation_correct(self):
        result = compute_category_sales(make_df())
        electronics = result[result["category"] == "Electronics"].iloc[0]["sales"]
        assert electronics == 175.0  # 100 + 75

    def test_output_columns(self):
        result = compute_category_sales(make_df())
        assert list(result.columns) == ["category", "sales"]


class TestComputeRegionSales:
    def test_sorted_descending(self):
        result = compute_region_sales(make_df())
        assert result["sales"].is_monotonic_decreasing

    def test_all_regions_present(self):
        result = compute_region_sales(make_df())
        assert set(result["region"]) == {"North", "South"}

    def test_aggregation_correct(self):
        result = compute_region_sales(make_df())
        north = result[result["region"] == "North"].iloc[0]["sales"]
        assert north == 175.0  # 100 + 75

    def test_output_columns(self):
        result = compute_region_sales(make_df())
        assert list(result.columns) == ["region", "sales"]
