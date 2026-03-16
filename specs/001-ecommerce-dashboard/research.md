# Research: E-Commerce Analytics Dashboard

**Branch**: `001-ecommerce-dashboard` | **Date**: 2026-03-16

---

## Decision 1: Streamlit Multi-Page App Structure

**Decision**: Use Streamlit's native multi-page support — `app.py` as the entry
point with a `pages/` directory containing one `.py` file per page.

**Rationale**: Streamlit automatically generates sidebar navigation from files
in `pages/`. File naming controls display order (numeric prefix) and page title
(filename after prefix). This requires zero custom routing code and is the
idiomatic Streamlit pattern as of v1.10+.

**Alternatives considered**:
- `st.navigation()` / manual routing in single file: More flexible but adds
  boilerplate; single-file grows unwieldy with 3+ pages.
- `st.tabs()`: Collapses multi-page into a tabbed layout — loses URL-per-page
  and browser history support.

**Key patterns**:
- `app.py`: Sets `st.set_page_config()`, shared config only.
- `pages/1_Overview.py`, `pages/2_Sales_Trend.py`, `pages/3_Breakdowns.py`:
  Each imports from `src/` modules; no business logic inline.
- Page title derived from filename: underscores → spaces, numeric prefix stripped.

---

## Decision 2: Data Module Layout

**Decision**: Two separate modules under `src/` — `src/loader.py` for CSV I/O
and `src/transforms.py` for all aggregation logic.

**Rationale**: Separating I/O from transformation is the single most important
boundary for testability. Unit tests can call `transforms.py` functions with
in-memory DataFrames without touching the filesystem. `loader.py` is the only
module that knows the file path.

**Note on naming**: The existing `data/` directory holds the source CSV. To
avoid a name conflict, Python modules live in `src/` rather than `data/`.

**Alternatives considered**:
- Single `utils.py`: Easier to start but mixes concerns; harder to unit-test
  transforms independently.
- Class-based `DataService`: Adds indirection with no benefit at this scale;
  YAGNI.

---

## Decision 3: File-Watch Reactivity via `mtime` Hashing

**Decision**: Use `@st.cache_data` with a helper that reads the file's
modification timestamp (`os.path.getmtime`) as the cache key. Streamlit
invalidates the cache automatically when the key changes.

**Rationale**: Polling a TTL would reload data on a schedule regardless of
whether the file changed (wasted work). Hashing full file contents (MD5) is
more accurate but reads the entire file just to compute the hash. `mtime` is
O(1) — a single `stat()` syscall — and accurate enough for a development/
analytics context where file writes are user-initiated.

**Implementation pattern**:
```python
# src/loader.py
import os, pandas as pd
import streamlit as st

def _get_mtime(path: str) -> float:
    return os.path.getmtime(path)

@st.cache_data
def load_data(path: str, _mtime: float) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["date"])

# Call site (in pages):
DATA_PATH = "data/sales-data.csv"
df = load_data(DATA_PATH, _mtime=_get_mtime(DATA_PATH))
```

The `_mtime` parameter (underscore prefix tells Streamlit not to hash it as
cache key) is passed explicitly so the cache busts when the file changes.
Actually: the correct pattern is the *opposite* — we DO want Streamlit to
include `_mtime` in the cache key. Streamlit skips hashing for args starting
with `_`, so we should pass mtime WITHOUT the underscore, or use a wrapper:

```python
@st.cache_data
def load_data(path: str, mtime: float) -> pd.DataFrame:
    # mtime is included in cache key; changes bust the cache
    return pd.read_csv(path, parse_dates=["date"])

df = load_data(DATA_PATH, mtime=os.path.getmtime(DATA_PATH))
```

**Alternatives considered**:
- TTL-based (`ttl=30`): Simple but wastes work; reloads even when file unchanged.
- MD5 hash: Accurate but reads full file contents for every check.
- No caching: Fine for 1k rows but unnecessary re-computation on every
  widget interaction; bad UX on slow connections.

---

## Decision 4: Dependency Management

**Decision**: `requirements.txt` only — pinned versions, committed to repo root.

**Rationale**: Streamlit Community Cloud reads `requirements.txt` at the repo
root by default. No additional configuration needed. `uv` is used locally
(`uv pip install -r requirements.txt`) but the file format is standard pip,
so it works everywhere.

**Minimum required packages**:
```
streamlit>=1.32.0
pandas>=2.0.0
plotly>=5.18.0
pytest>=8.0.0
```

**Alternatives considered**:
- `pyproject.toml` + exported `requirements.txt`: Adds a sync step; easy to
  forget to re-export before pushing.
- `uv.lock` only: Streamlit Cloud does not support `uv.lock` natively.

---

## Decision 5: Error Handling Strategy

**Decision**: Validate CSV existence and schema in `loader.py` before returning
a DataFrame. Raise a descriptive `ValueError` with actionable instructions.
Each page catches this at the top and calls `st.error()` + `st.stop()` to
halt rendering cleanly.

**Validation checks**:
1. File exists at expected path.
2. File is readable and parseable as CSV.
3. Required columns present: `date`, `order_id`, `product`, `category`,
   `region`, `quantity`, `unit_price`, `total_amount`.
4. `date` column parseable as dates.
5. `total_amount` column is numeric.

**Error message format**:
```
Data file error: [specific problem]
Expected file: data/sales-data.csv
[Corrective instruction]
```
