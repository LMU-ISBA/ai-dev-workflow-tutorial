# Data Interface Contract: Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-25
**Type**: File-based data contract (no REST API)

## Overview

This dashboard does not expose an API. Instead, it consumes data from a CSV file. This contract defines the expected file format and data structure.

---

## Input Contract: sales-data.csv

### File Location

```
data/sales-data.csv
```

### File Format

- **Encoding**: UTF-8
- **Delimiter**: Comma (`,`)
- **Header Row**: Required (first row)
- **Quote Character**: Double quote (`"`) for fields containing commas

### Column Specification

| Column | Type | Required | Format | Example |
|--------|------|----------|--------|---------|
| `date` | string | Yes | YYYY-MM-DD | 2024-01-15 |
| `order_id` | string | Yes | ORD-NNNNNN | ORD-001234 |
| `product` | string | Yes | Free text | Wireless Headphones |
| `category` | string | Yes | Enumerated | Electronics |
| `region` | string | Yes | Enumerated | North |
| `quantity` | integer | Yes | Positive integer | 2 |
| `unit_price` | decimal | Yes | Positive decimal | 49.99 |
| `total_amount` | decimal | Yes | Positive decimal | 99.98 |

### Valid Category Values

```
Electronics
Accessories
Audio
Wearables
Smart Home
```

### Valid Region Values

```
North
South
East
West
```

### Sample Valid Input

```csv
date,order_id,product,category,region,quantity,unit_price,total_amount
2024-01-03,ORD-001001,Wireless Earbuds,Audio,North,2,79.99,159.98
2024-01-03,ORD-001002,Phone Case,Accessories,South,3,24.99,74.97
```

---

## Output Contract: Dashboard Views

The dashboard produces visual outputs (not data exports). These are the expected visualizations:

### KPI Cards

| Metric | Source Calculation | Display Format |
|--------|-------------------|----------------|
| Total Sales | `SUM(total_amount)` | $XXX,XXX.XX |
| Total Orders | `COUNT(order_id)` | X,XXX |

### Sales Trend Chart

| Property | Value |
|----------|-------|
| Chart Type | Line |
| X-Axis | Month (YYYY-MM) |
| Y-Axis | Total Sales ($) |
| Data Points | One per month |
| Tooltip | Month, Sales Amount |

### Category Breakdown Chart

| Property | Value |
|----------|-------|
| Chart Type | Horizontal Bar |
| Categories | 5 (sorted by value, descending) |
| Values | Sum of total_amount per category |
| Tooltip | Category Name, Sales Amount |

### Region Breakdown Chart

| Property | Value |
|----------|-------|
| Chart Type | Horizontal Bar |
| Regions | 4 (sorted by value, descending) |
| Values | Sum of total_amount per region |
| Tooltip | Region Name, Sales Amount |

---

## Error Handling Contract

| Input Condition | Expected Behavior |
|-----------------|-------------------|
| File not found | Display error: "Sales data file not found" |
| Empty file (headers only) | Display zeros for KPIs, empty charts |
| Missing required column | Display error identifying missing column |
| Invalid date format | Attempt flexible parsing, exclude unparseable rows |
| Invalid numeric value | Exclude row from calculations |
| Unknown category/region | Include in calculations, display as-is |

---

## Compatibility Notes

- Dashboard reads CSV synchronously on startup
- No real-time updates (refresh page to reload data)
- No write operations to the data file
- File must be accessible at relative path from app.py
