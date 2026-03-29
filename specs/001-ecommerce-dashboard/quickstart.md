# Quickstart: E-Commerce Analytics Dashboard

**Branch**: `001-ecommerce-dashboard` | **Date**: 2026-03-16

Use this guide to run the dashboard locally and verify it works end-to-end.

---

## Prerequisites

- Python 3.11+
- `uv` installed (`pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- The repo cloned and checked out to branch `001-ecommerce-dashboard`

---

## Setup

```bash
# 1. Install dependencies
uv pip install -r requirements.txt

# 2. Confirm the data file exists
ls data/sales-data.csv
```

---

## Run Locally

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## Validation Checklist

Work through each item to confirm the dashboard is functioning correctly.

### Overview Page

- [ ] Page loads without errors
- [ ] "Total Sales" is displayed as a formatted currency value (e.g., `$652,340`)
- [ ] "Total Orders" is displayed as a whole number (e.g., `482`)
- [ ] Values match manual spot-check: open `data/sales-data.csv`, sum
      `total_amount` and count rows

### Sales Trend Page

- [ ] Page loads without errors
- [ ] Line chart renders with time on X-axis and sales on Y-axis
- [ ] Chart defaults to **Monthly** granularity
- [ ] Switching to **Daily** updates the chart without a page reload
- [ ] Hovering a data point shows a tooltip with exact date and sales value

### Breakdowns Page

- [ ] Page loads without errors
- [ ] "Sales by Category" bar chart shows all 5 categories
- [ ] Categories are sorted highest-to-lowest
- [ ] "Sales by Region" bar chart shows all 4 regions
- [ ] Regions are sorted highest-to-lowest
- [ ] Hovering a bar shows the category/region name and exact value

### File-Watch Reactivity

- [ ] With the dashboard open, edit `data/sales-data.csv` (change one
      `total_amount` value and save)
- [ ] Within ~30 seconds the KPI on the Overview page updates automatically

### Error Handling

- [ ] Temporarily rename `data/sales-data.csv` to `data/sales-data.csv.bak`
- [ ] Reload any dashboard page — a clear error message appears with
      instructions; no partial data is shown
- [ ] Restore the file — dashboard recovers automatically

---

## Deploy to Streamlit Cloud

1. Push branch `001-ecommerce-dashboard` to GitHub (or merge to `main`).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Select your repo, branch, and set **Main file path** to `app.py`.
4. Click **Deploy**. No secrets or environment variables required.
5. Run the validation checklist above against the deployed URL.
