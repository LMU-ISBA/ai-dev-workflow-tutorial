# Data Model: E-Commerce Analytics Dashboard

**Branch**: `001-ecommerce-dashboard` | **Date**: 2026-03-16

---

## Source Entity: Transaction

Represents a single sales record loaded directly from `data/sales-data.csv`.
This is the raw, unmodified row shape from the CSV.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `date` | date | Transaction date | Required; parseable as YYYY-MM-DD |
| `order_id` | string | Unique order identifier | Required; non-empty |
| `product` | string | Product name | Required; non-empty |
| `category` | string | Product category | Required; one of 5 known values |
| `region` | string | Geographic region | Required; one of 4 known values |
| `quantity` | integer | Units sold | Required; positive integer |
| `unit_price` | decimal | Price per unit | Required; positive number |
| `total_amount` | decimal | Total transaction value | Required; positive number |

**Validation rules**:
- All 8 columns MUST be present; missing columns raise a descriptive error.
- `date` MUST be parseable as a date; non-date values raise an error.
- `total_amount` MUST be numeric; non-numeric values raise an error.
- Rows with null values in `total_amount`, `date`, `category`, or `region`
  are dropped with a warning (not a fatal error).

**Known domain values**:
- Categories: `Electronics`, `Accessories`, `Audio`, `Wearables`, `Smart Home`
- Regions: `North`, `South`, `East`, `West`

---

## Derived Entity: KPI Result

Computed from all Transactions in the dataset. Used by the Overview page.

| Field | Type | Description | Derivation |
|-------|------|-------------|------------|
| `total_sales` | decimal | Sum of all `total_amount` values | `df["total_amount"].sum()` |
| `total_orders` | integer | Count of all rows | `len(df)` |

---

## Derived Entity: Time Series Point

One data point in the Sales Trend chart. The full time series is a list of
these points, grouped by either day or month.

| Field | Type | Description | Derivation |
|-------|------|-------------|------------|
| `period` | date | Start of the day or month | `df["date"]` grouped by day or month-start |
| `sales` | decimal | Sum of `total_amount` for the period | `groupby(period)["total_amount"].sum()` |

**Granularities**:
- **Daily**: Group by calendar date; one point per day with transactions.
- **Monthly**: Group by year-month (period start); one point per month.

---

## Derived Entity: Category Aggregate

One bar in the Sales by Category chart.

| Field | Type | Description | Derivation |
|-------|------|-------------|------------|
| `category` | string | Product category name | `df["category"]` |
| `sales` | decimal | Sum of `total_amount` for category | `groupby("category")["total_amount"].sum()` |

**Ordering**: Sorted descending by `sales`. All categories present in the
dataset are included, even if their sales total is zero.

---

## Derived Entity: Region Aggregate

One bar in the Sales by Region chart.

| Field | Type | Description | Derivation |
|-------|------|-------------|------------|
| `region` | string | Geographic region name | `df["region"]` |
| `sales` | decimal | Sum of `total_amount` for region | `groupby("region")["total_amount"].sum()` |

**Ordering**: Sorted descending by `sales`. All regions present in the
dataset are included.

---

## Data Flow

```
data/sales-data.csv
        │
        ▼
src/loader.py::load_data()
  • Reads CSV
  • Validates schema + types
  • Returns raw DataFrame (Transaction shape)
        │
        ├──► src/transforms.py::compute_kpis(df)
        │         Returns: KPI Result
        │
        ├──► src/transforms.py::compute_time_series(df, granularity)
        │         granularity: "daily" | "monthly"
        │         Returns: list[Time Series Point] as DataFrame
        │
        ├──► src/transforms.py::compute_category_sales(df)
        │         Returns: Category Aggregate DataFrame
        │
        └──► src/transforms.py::compute_region_sales(df)
                  Returns: Region Aggregate DataFrame
```
