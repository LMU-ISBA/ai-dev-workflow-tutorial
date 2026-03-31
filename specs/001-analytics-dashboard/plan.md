# Implementation Plan: ShopSmart Sales Analytics Dashboard

**Branch**: `001-analytics-dashboard` | **Date**: 2026-03-30 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-analytics-dashboard/spec.md`

## Summary

Build a two-file Streamlit dashboard (`data.py` + `app.py`) at the repo root that
loads `data/sales-data.csv`, computes four aggregations via pandas, and renders
three Plotly charts plus two KPI scorecards for executive stakeholders. Deploy to
Streamlit Community Cloud for a public URL.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: streamlit, pandas, plotly
**Storage**: Static CSV file — `data/sales-data.csv` (no database)
**Testing**: Manual validation via `quickstart.md` checklist (no automated tests in scope)
**Target Platform**: Web browser (desktop); hosted on Streamlit Community Cloud
**Project Type**: Web application (single-page dashboard)
**Performance Goals**: Full dashboard visible within 5 seconds of page load (SC-001)
**Constraints**: No DB connections; no external APIs; CSV-only data source (Constitution V)
**Scale/Scope**: ~1,000 transaction rows; single user at a time; single data file

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Check | Status |
|-----------|-------|--------|
| I. Executive Clarity | All charts sorted, labeled, and tooltip-enabled; no raw tables exposed | ✅ Pass |
| II. Data Accuracy | All KPIs/charts derive from raw CSV via `groupby`; no approximations | ✅ Pass |
| III. Spec-Driven Development | spec.md written and approved before this plan | ✅ Pass |
| IV. Minimal Dependencies | Only streamlit, pandas, plotly — each strictly necessary | ✅ Pass |
| V. Static CSV Data Source | `data/sales-data.csv` only; no DB or API connections | ✅ Pass |

No violations. Complexity Tracking table not required.

## Project Structure

### Documentation (this feature)

```text
specs/001-analytics-dashboard/
├── plan.md              # This file
├── research.md          # Technology decisions (Phase 0)
├── data-model.md        # Entity definitions and aggregations (Phase 1)
├── quickstart.md        # Local setup and validation guide (Phase 1)
└── tasks.md             # Task list (/speckit.tasks — not yet generated)
```

### Source Code (repository root)

```text
app.py                   # Streamlit UI: layout, KPI cards, chart rendering
data.py                  # Data layer: CSV loading, aggregations, caching
data/
└── sales-data.csv       # Source dataset (already present)
requirements.txt         # Pinned dependencies
```

**Structure Decision**: Flat two-file layout at repo root. `data.py` owns all
pandas logic and `@st.cache_data`; `app.py` owns all Streamlit layout and Plotly
rendering. No subdirectories needed at this scope. Streamlit Community Cloud
auto-detects `app.py` at repo root with no extra configuration.

## Phase 0: Research (Complete)

All technology decisions resolved. See [research.md](research.md).

Key decisions:
- **Charts**: Plotly via `plotly.express` — interactive tooltips, Streamlit-native
- **Structure**: `data.py` + `app.py` at repo root — clean separation, easy deploy
- **Python**: 3.11 — stable, PRD-recommended
- **Caching**: `@st.cache_data` on CSV load function
- **Aggregations**: pandas `groupby` in `data.py`; results passed as DataFrames to `app.py`

## Phase 1: Design (Complete)

### data.py — Data Layer Contract

`data.py` MUST expose these functions:

```
load_data() -> pd.DataFrame
  Loads data/sales-data.csv; cached with @st.cache_data.
  Returns cleaned DataFrame with null total_amount rows removed.
  Raises a descriptive error if file is missing.

get_kpis(df) -> dict[str, float|int]
  Returns {"total_sales": float, "total_orders": int}

get_monthly_trend(df) -> pd.DataFrame
  Columns: ["month" (str, "YYYY-MM"), "sales" (float)]
  12 rows, sorted ascending by month.

get_category_breakdown(df) -> pd.DataFrame
  Columns: ["category" (str), "sales" (float)]
  5 rows, sorted descending by sales.

get_region_breakdown(df) -> pd.DataFrame
  Columns: ["region" (str), "sales" (float)]
  4 rows, sorted descending by sales.
```

### app.py — UI Layout Contract

```
Page title:  "ShopSmart Sales Dashboard"
Row 1:       st.columns(2) → Total Sales card | Total Orders card
Row 2:       Full-width Plotly line chart (monthly trend)
Row 3:       st.columns(2) → Category bar chart | Region bar chart
```

KPI card format:
- `st.metric(label="Total Sales", value="$672,345")`
- `st.metric(label="Total Orders", value="482")`

Chart requirements:
- All charts use `st.plotly_chart(fig, use_container_width=True)`
- Hover tooltips enabled on all charts (Plotly default behavior)
- Axes labeled; chart titles present

### Artifact Summary

| Artifact | Status |
|----------|--------|
| research.md | ✅ Complete |
| data-model.md | ✅ Complete |
| quickstart.md | ✅ Complete |
| contracts/ | N/A — internal app, no external API surface |
| tasks.md | ⏳ Pending — run `/speckit.tasks` |
