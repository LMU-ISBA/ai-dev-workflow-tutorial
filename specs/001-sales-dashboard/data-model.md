# Data Model: E-Commerce Analytics Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-25
**Status**: Complete

## Overview

This document defines the data structures used in the sales dashboard. The primary data source is a CSV file containing sales transaction records.

---

## Primary Entity: Transaction

A transaction represents a single sales order in the ShopSmart e-commerce system.

### Schema

| Field | Type | Description | Example | Constraints |
|-------|------|-------------|---------|-------------|
| `date` | Date | Transaction date | 2024-01-15 | Required, YYYY-MM-DD format |
| `order_id` | String | Unique order identifier | ORD-001234 | Required, unique |
| `product` | String | Product name | Wireless Headphones | Required |
| `category` | String | Product category | Electronics | Required, one of 5 values |
| `region` | String | Geographic region | North | Required, one of 4 values |
| `quantity` | Integer | Units sold | 2 | Required, positive integer |
| `unit_price` | Decimal | Price per unit | 49.99 | Required, positive decimal |
| `total_amount` | Decimal | Total transaction value | 99.98 | Required, equals quantity × unit_price |

### Category Values (Enumeration)

| Value | Description |
|-------|-------------|
| Electronics | Electronic devices (tablets, keyboards, mice) |
| Accessories | Device accessories (cables, cases, chargers) |
| Audio | Audio equipment (headphones, speakers, earbuds) |
| Wearables | Wearable technology (watches, trackers, rings) |
| Smart Home | Home automation devices (thermostats, doorbells, plugs) |

### Region Values (Enumeration)

| Value | Description |
|-------|-------------|
| North | Northern geographic territory |
| South | Southern geographic territory |
| East | Eastern geographic territory |
| West | Western geographic territory |

---

## Derived Data Structures

These structures are computed from the raw transaction data for visualization purposes.

### KPI Metrics

| Metric | Calculation | Format |
|--------|-------------|--------|
| Total Sales | `SUM(total_amount)` | Currency ($X,XXX,XXX.XX) |
| Total Orders | `COUNT(order_id)` | Integer with separators |

### Monthly Sales Aggregation

Used for the sales trend line chart.

| Field | Type | Description |
|-------|------|-------------|
| `month` | Period | Year-month (e.g., 2024-01) |
| `total_sales` | Decimal | Sum of total_amount for the month |

**Computation**:
```
GROUP BY month(date)
AGGREGATE SUM(total_amount)
ORDER BY month ASC
```

### Category Sales Aggregation

Used for the sales by category bar chart.

| Field | Type | Description |
|-------|------|-------------|
| `category` | String | Product category name |
| `total_sales` | Decimal | Sum of total_amount for the category |

**Computation**:
```
GROUP BY category
AGGREGATE SUM(total_amount)
ORDER BY total_sales DESC
```

### Region Sales Aggregation

Used for the sales by region bar chart.

| Field | Type | Description |
|-------|------|-------------|
| `region` | String | Geographic region name |
| `total_sales` | Decimal | Sum of total_amount for the region |

**Computation**:
```
GROUP BY region
AGGREGATE SUM(total_amount)
ORDER BY total_sales DESC
```

---

## Data Validation Rules

### Required Field Validation

All fields in the Transaction schema are required. Rows with missing values should be:
- Logged as warnings (if logging is implemented)
- Excluded from calculations
- Not cause application failure

### Type Validation

| Field | Validation |
|-------|------------|
| `date` | Must parse as valid date |
| `quantity` | Must be positive integer |
| `unit_price` | Must be positive decimal |
| `total_amount` | Must be positive decimal |

### Referential Validation

| Field | Valid Values |
|-------|--------------|
| `category` | Electronics, Accessories, Audio, Wearables, Smart Home |
| `region` | North, South, East, West |

Rows with invalid category or region values should be processed but may appear as unexpected categories/regions in visualizations.

---

## Data Volume Expectations

| Metric | Expected Value |
|--------|----------------|
| Total Records | ~500 transactions |
| Date Range | 12 months |
| File Size | <1 MB |
| Categories | 5 distinct values |
| Regions | 4 distinct values |

---

## Sample Data

```csv
date,order_id,product,category,region,quantity,unit_price,total_amount
2024-01-03,ORD-001001,Wireless Earbuds,Audio,North,2,79.99,159.98
2024-01-03,ORD-001002,Phone Case,Accessories,South,3,24.99,74.97
2024-01-04,ORD-001003,Smart Watch,Wearables,East,1,299.99,299.99
2024-01-04,ORD-001004,USB-C Cable,Accessories,West,5,12.99,64.95
```

---

## Relationships

```
Transaction (1) ──belongs to──> (1) Category
Transaction (1) ──located in──> (1) Region
Transaction (1) ──occurred on──> (1) Date
```

Note: These are logical relationships for understanding the data model. No foreign key constraints exist in the CSV format.
