# Implementation Plan: E-Commerce Analytics Dashboard

**Branch**: `001-ecommerce-dashboard` | **Date**: 2026-03-16 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-ecommerce-dashboard/spec.md`

---

## Summary

Build a publicly accessible, three-page Streamlit dashboard for ShopSmart sales
data. The app reads `data/sales-data.csv`, auto-reloads on file change via
`mtime`-based cache invalidation, and visualizes KPIs, sales trends (daily/monthly
toggle), and category/regional breakdowns using Plotly Express. Deployed to
Streamlit Community Cloud from `requirements.txt`.

---

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Streamlit ≥1.32, pandas ≥2.0, Plotly ≥5.18, pytest ≥8.0
**Storage**: CSV file (`data/sales-data.csv`) — no database
**Testing**: pytest; unit tests for `src/loader.py` and `src/transforms.py` only
**Target Platform**: Streamlit Community Cloud (public, free tier)
**Project Type**: Web application (Streamlit multi-page app)
**Performance Goals**: Full dashboard load < 5s; granularity toggle < 1s
**Constraints**: `requirements.txt` only (no Docker, no system packages); all
secrets via `st.secrets` if ever needed; no user authentication
**Scale/Scope**: ~1,000 CSV rows; single concurrent user expected; 3 pages

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|-----------|------|--------|
| I. CSV-First Data Layer | Data sourced exclusively from `data/sales-data.csv`; no DB or API calls | ✅ Pass |
| II. File-Watch Reactivity | `mtime`-based `@st.cache_data` invalidation; no manual reload button | ✅ Pass |
| III. Visualization-Driven Design | Every page produces KPIs or charts; no raw tables exposed in UI | ✅ Pass |
| IV. Unit-Tested Transformations | `tests/unit/test_loader.py` + `tests/unit/test_transforms.py` cover all aggregation functions | ✅ Pass |
| V. Streamlit Cloud First | `requirements.txt` only; no Docker; no system dependencies; deployable from repo root | ✅ Pass |

No violations. Complexity Tracking table not required.

---

## Project Structure

### Documentation (this feature)

```text
specs/001-ecommerce-dashboard/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── module-contracts.md   # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
app.py                        # Entry point — st.set_page_config(), shared config

pages/
├── 1_Overview.py             # Total Sales + Total Orders KPI scorecards
├── 2_Sales_Trend.py          # Line chart with daily/monthly toggle
└── 3_Breakdowns.py           # Sales by category + sales by region bar charts

src/
├── loader.py                 # CSV loading; mtime-based cache invalidation; schema validation
└── transforms.py             # compute_kpis, compute_time_series, compute_category_sales,
                              # compute_region_sales

tests/
└── unit/
    ├── test_loader.py        # Tests for schema validation + error cases
    └── test_transforms.py    # Tests for all four transform functions

data/
└── sales-data.csv            # Source dataset (already exists)

requirements.txt              # Pinned dependencies for local + Streamlit Cloud
```

**Structure Decision**: Single Streamlit app using the native `pages/` multi-page
pattern. Business logic is split into `src/loader.py` (I/O) and
`src/transforms.py` (aggregations) to keep pages thin and transformations
independently testable. The `data/` directory is reserved for CSV source files
only; Python modules live in `src/` to avoid a namespace conflict.

---

## Complexity Tracking

> No constitution violations. This section intentionally left empty.
