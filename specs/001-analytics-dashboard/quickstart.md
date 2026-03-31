# Quickstart: ShopSmart Sales Analytics Dashboard

**Branch**: `001-analytics-dashboard` | **Date**: 2026-03-30

Use this guide to verify the dashboard works end-to-end after implementation.

## Prerequisites

- Python 3.11 installed
- Repository cloned and on branch `001-analytics-dashboard`
- `data/sales-data.csv` present at the repo root

## Local Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the dashboard
streamlit run app.py
```

The dashboard opens at `http://localhost:8501` in your default browser.

## Validation Checklist

Run through these checks after the app loads:

- [ ] **KPI cards visible**: Two metric cards appear at the top of the page
- [ ] **Total Sales**: Displays a currency value in the range `$650,000–$700,000`
- [ ] **Total Orders**: Displays `482`
- [ ] **Trend chart**: A line chart with 12 monthly data points (Jan–Dec 2024) appears
- [ ] **Trend tooltips**: Hovering a data point shows the exact monthly sales amount
- [ ] **Category chart**: A bar chart with 5 bars appears, sorted highest to lowest
- [ ] **Region chart**: A bar chart with 4 bars appears, sorted highest to lowest
- [ ] **Side-by-side layout**: Category and Region charts appear in two columns
- [ ] **Bar tooltips**: Hovering a bar shows the exact sales amount
- [ ] **No errors**: No red error banners or Python tracebacks visible

## Expected Values (from sample data)

| Metric         | Expected                        |
|----------------|---------------------------------|
| Total Sales    | ~$116,500                       |
| Total Orders   | 482                             |
| Top Category   | Electronics or Audio            |
| Regions shown  | North, South, East, West        |
| Trend months   | Jan 2024 through Dec 2024       |

## Deployment to Streamlit Community Cloud

1. Push branch to GitHub and merge to `main`
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in
3. Click **New app** → select your repo → set main file to `app.py`
4. Click **Deploy** — the app gets a public URL automatically

Once deployed, re-run the validation checklist against the live URL.
