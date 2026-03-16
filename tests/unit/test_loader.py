import os

import pandas as pd
import pytest

from src.loader import load_data

REQUIRED_COLUMNS = [
    "date", "order_id", "product", "category",
    "region", "quantity", "unit_price", "total_amount",
]


def write_valid_csv(path):
    with open(path, "w") as f:
        f.write(",".join(REQUIRED_COLUMNS) + "\n")
        f.write("2024-01-01,ORD-001,Widget A,Electronics,North,1,100.0,100.0\n")
        f.write("2024-01-15,ORD-002,Widget B,Audio,South,2,50.0,100.0\n")


class TestLoadData:
    def test_file_not_found_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            load_data(str(tmp_path / "nonexistent.csv"), mtime=0.0)

    def test_missing_columns_raises_value_error(self, tmp_path):
        csv = tmp_path / "bad.csv"
        csv.write_text("date,order_id\n2024-01-01,ORD-001\n")
        with pytest.raises(ValueError, match="missing required columns"):
            load_data(str(csv), mtime=os.path.getmtime(str(csv)))

    def test_non_numeric_total_amount_raises_value_error(self, tmp_path):
        csv = tmp_path / "bad.csv"
        csv.write_text(
            ",".join(REQUIRED_COLUMNS) + "\n"
            "2024-01-01,ORD-001,Widget,Electronics,North,1,100.0,not_a_number\n"
        )
        with pytest.raises(ValueError, match="total_amount"):
            load_data(str(csv), mtime=os.path.getmtime(str(csv)))

    def test_successful_load_returns_dataframe(self, tmp_path):
        csv = tmp_path / "sales.csv"
        write_valid_csv(str(csv))
        df = load_data(str(csv), mtime=os.path.getmtime(str(csv)))
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 2

    def test_successful_load_date_is_datetime(self, tmp_path):
        csv = tmp_path / "sales.csv"
        write_valid_csv(str(csv))
        df = load_data(str(csv), mtime=os.path.getmtime(str(csv)))
        assert pd.api.types.is_datetime64_any_dtype(df["date"])

    def test_successful_load_total_amount_is_numeric(self, tmp_path):
        csv = tmp_path / "sales.csv"
        write_valid_csv(str(csv))
        df = load_data(str(csv), mtime=os.path.getmtime(str(csv)))
        assert pd.api.types.is_float_dtype(df["total_amount"])

    def test_all_required_columns_present(self, tmp_path):
        csv = tmp_path / "sales.csv"
        write_valid_csv(str(csv))
        df = load_data(str(csv), mtime=os.path.getmtime(str(csv)))
        for col in REQUIRED_COLUMNS:
            assert col in df.columns
