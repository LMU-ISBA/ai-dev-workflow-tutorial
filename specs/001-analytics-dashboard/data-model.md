# Data Model: ShopSmart Sales Analytics Dashboard

**Branch**: `001-analytics-dashboard` | **Date**: 2026-03-30

## Source Entity: Transaction

Represents a single sale event. Read directly from `data/sales-data.csv`.

| Field          | Type     | Description                          | Example          | Validation                  |
|----------------|----------|--------------------------------------|------------------|-----------------------------|
| `date`         | date     | Transaction date                     | `2024-01-15`     | MUST be parseable as date   |
| `order_id`     | string   | Unique order identifier              | `ORD-001234`     | Non-null                    |
| `product`      | string   | Product name                         | `Wireless Headphones` | Non-null              |
| `category`     | string   | Product category                     | `Electronics`    | One of 5 known values       |
| `region`       | string   | Geographic region                    | `North`          | One of 4 known values       |
| `quantity`     | integer  | Units sold in this transaction       | `2`              | Positive integer            |
| `unit_price`   | decimal  | Price per unit in USD                | `49.99`          | Positive decimal            |
| `total_amount` | decimal  | Total transaction value (`qty × price`) | `99.98`       | Positive decimal; non-null for KPI inclusion |

**Null handling**: Rows with null or non-numeric `total_amount` MUST be excluded
from all aggregations. The count of excluded rows MUST be surfaced to the user.

---

## Derived Entities (computed by `data.py`)

### KPI Summary

Scalar values computed from all valid Transaction rows.

| Field           | Computation                    | Used By         |
|-----------------|-------------------------------|-----------------|
| `total_sales`   | `SUM(total_amount)`            | Total Sales KPI |
| `total_orders`  | `COUNT(order_id)`              | Total Orders KPI |

### Monthly Aggregate

One row per calendar month. Used by the Sales Trend line chart.

| Field          | Computation                              | Used By        |
|----------------|------------------------------------------|----------------|
| `month`        | `date` truncated to month (YYYY-MM)      | x-axis label   |
| `sales`        | `SUM(total_amount)` grouped by month     | y-axis value   |

- Sorted ascending by `month`
- All 12 months of 2024 MUST be present (zero-filled if a month has no data)

### Category Aggregate

One row per product category. Used by the Category bar chart.

| Field      | Computation                                  | Used By       |
|------------|----------------------------------------------|---------------|
| `category` | Distinct values of `category`                | x-axis label  |
| `sales`    | `SUM(total_amount)` grouped by `category`    | bar height    |

- Sorted descending by `sales`
- All 5 known categories MUST appear (zero-filled if absent in data)

### Region Aggregate

One row per geographic region. Used by the Region bar chart.

| Field    | Computation                               | Used By       |
|----------|-------------------------------------------|---------------|
| `region` | Distinct values of `region`               | x-axis label  |
| `sales`  | `SUM(total_amount)` grouped by `region`   | bar height    |

- Sorted descending by `sales`
- All 4 known regions MUST appear (zero-filled if absent in data)

---

## Known Category Values

| Category    |
|-------------|
| Electronics |
| Accessories |
| Audio       |
| Wearables   |
| Smart Home  |

## Known Region Values

| Region |
|--------|
| North  |
| South  |
| East   |
| West   |
