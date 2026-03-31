# Research: ShopSmart Sales Analytics Dashboard

**Branch**: `001-analytics-dashboard` | **Date**: 2026-03-30

## Technology Decisions

### Charting Library

**Decision**: Plotly (`plotly`) via `plotly.express`
**Rationale**: Plotly is the only option that satisfies FR-006 and FR-009 (interactive
hover tooltips on line and bar charts) while integrating natively with Streamlit via
`st.plotly_chart`. The PRD explicitly recommends it. It produces professional,
executive-quality visuals out of the box.
**Alternatives considered**:
- Altair: Also supports tooltips and Streamlit integration, but less familiar to
  most Python data teams and not the PRD recommendation.
- Matplotlib/Seaborn: Static only — cannot satisfy tooltip requirements. Ruled out.

### Code Structure

**Decision**: Two-file flat layout at repo root — `data.py` + `app.py`
**Rationale**: Cleanly separates data concerns (loading, aggregation) from presentation
(layout, charts). Each file has a single responsibility. Flat repo-root placement is
the path of least resistance for Streamlit Community Cloud deployment — no extra
`streamlit_app.py` shim or `[server]` config needed.
**Alternatives considered**:
- Single file: Simpler but mixes data logic with UI, making future maintenance harder.
- `src/` package: Adds indirection with no benefit at this scope (2 files, 1 developer).

### Python Version

**Decision**: Python 3.11
**Rationale**: Stable, well-supported, and explicitly recommended in the PRD. All
required libraries (streamlit, pandas, plotly) have first-class 3.11 support.
**Alternatives considered**:
- Python 3.12: Minor performance gains but slightly less ecosystem maturity.
- Python 3.10: No advantage over 3.11; older.

### Streamlit Caching Strategy

**Decision**: Use `@st.cache_data` on the data-loading function in `data.py`
**Rationale**: The constitution (Principle V) mandates a static CSV source. Caching
prevents the file from being re-read on every UI interaction, keeping load times
within the 5-second SC-001 target. Cache is invalidated automatically when the
file changes.
**Alternatives considered**:
- No caching: Would re-read CSV on every widget interaction — unnecessary I/O.
- `@st.cache_resource`: Intended for non-data resources (DB connections, models);
  wrong semantic for a DataFrame.

### Data Aggregation Approach

**Decision**: All aggregations computed in `data.py` using pandas `groupby` +
`sum`/`count`; results returned as DataFrames passed into Plotly functions in `app.py`
**Rationale**: Keeps `app.py` free of business logic. Each aggregation maps 1:1 to a
chart or KPI (monthly totals, category totals, region totals, overall totals).
**Alternatives considered**:
- Inline aggregation in `app.py`: Works but conflates data and presentation layers.
- Pre-aggregated CSV: Defeats the single-source-of-truth principle (Constitution II).

### Deployment

**Decision**: Streamlit Community Cloud, connected to the GitHub `main` branch
**Rationale**: Specified in the PRD (NFR-5) and the spec (SC-005). Free tier supports
public apps from public GitHub repos. Auto-deploys on push to `main`.
**Alternatives considered**:
- Heroku / Render: More configuration required; Streamlit Cloud is purpose-built.
- Local only: Does not meet SC-005 (public URL requirement).
