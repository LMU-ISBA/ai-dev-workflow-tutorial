# Module Contracts: E-Commerce Analytics Dashboard

**Branch**: `001-ecommerce-dashboard` | **Date**: 2026-03-16

These contracts define the public function signatures for the two shared
modules. Page files MUST only call functions listed here; internal helpers
are not part of the contract.

---

## `src/loader.py`

### `load_data(path: str, mtime: float) -> pd.DataFrame`

Loads and validates the sales CSV. The `mtime` parameter is included in
Streamlit's cache key so the cache busts when the file changes on disk.

**Parameters**:
- `path` — absolute or repo-relative path to the CSV file.
- `mtime` — file modification timestamp from `os.path.getmtime(path)`.
  Must be passed by the caller; `load_data` does not read mtime itself.

**Returns**: A validated DataFrame with columns:
`date (datetime64)`, `order_id (str)`, `product (str)`, `category (str)`,
`region (str)`, `quantity (int)`, `unit_price (float)`, `total_amount (float)`

**Raises**:
- `FileNotFoundError` — if `path` does not exist.
- `ValueError` — if required columns are missing or types are invalid.
  Message format: `"Data file error: <reason>\nExpected file: <path>\n<instruction>"`

**Cache behaviour**: Decorated with `@st.cache_data`. Cache is invalidated
whenever `mtime` changes.

---

## `src/transforms.py`

### `compute_kpis(df: pd.DataFrame) -> dict`

**Parameters**: `df` — validated DataFrame from `load_data`.

**Returns**:
```python
{
    "total_sales": float,   # sum of total_amount
    "total_orders": int,    # len(df)
}
```

---

### `compute_time_series(df: pd.DataFrame, granularity: str) -> pd.DataFrame`

**Parameters**:
- `df` — validated DataFrame from `load_data`.
- `granularity` — `"daily"` or `"monthly"`.

**Returns**: DataFrame with columns:
- `period (datetime64)` — start of the day or month.
- `sales (float)` — sum of `total_amount` for that period.

Sorted ascending by `period`.

**Raises**: `ValueError` if `granularity` is not `"daily"` or `"monthly"`.

---

### `compute_category_sales(df: pd.DataFrame) -> pd.DataFrame`

**Parameters**: `df` — validated DataFrame from `load_data`.

**Returns**: DataFrame with columns:
- `category (str)`
- `sales (float)` — sum of `total_amount` per category.

Sorted descending by `sales`.

---

### `compute_region_sales(df: pd.DataFrame) -> pd.DataFrame`

**Parameters**: `df` — validated DataFrame from `load_data`.

**Returns**: DataFrame with columns:
- `region (str)`
- `sales (float)` — sum of `total_amount` per region.

Sorted descending by `sales`.
