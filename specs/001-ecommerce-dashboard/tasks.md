# Tasks: E-Commerce Analytics Dashboard

**Input**: Design documents from `specs/001-ecommerce-dashboard/`
**Prerequisites**: plan.md ✅ | spec.md ✅ | research.md ✅ | data-model.md ✅ | contracts/ ✅

**Tests**: Included after implementation for `transforms.py` and `loader.py` (unit tests only, per constitution).

**Organization**: Tasks follow the data flow within each page (one task per function call the page makes). Each user story phase is independently testable.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Exact file paths included in all descriptions

## Path Conventions

- Single project layout: `app.py`, `pages/`, `src/`, `tests/unit/` at repository root

---

## Phase 1: Setup

**Purpose**: Project initialization and file structure

- [x] T001 Create project directory structure — stub files: `app.py`, `pages/1_Overview.py`, `pages/2_Sales_Trend.py`, `pages/3_Breakdowns.py`, `src/__init__.py`, `tests/__init__.py`, `tests/unit/__init__.py`
- [x] T002 [P] Create `requirements.txt` with pinned dependencies: `streamlit>=1.32.0`, `pandas>=2.0.0`, `plotly>=5.18.0`, `pytest>=8.0.0`
- [x] T003 [P] Implement `app.py` — call `st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")` as the sole entry point; no page logic here

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared data modules that ALL user story pages depend on

**⚠️ CRITICAL**: No page work can begin until this phase is complete

- [x] T004 [P] Implement `src/loader.py` — define `load_data(path: str, mtime: float) -> pd.DataFrame` decorated with `@st.cache_data`; read CSV with `pd.read_csv(path, parse_dates=["date"])`; validate required columns (`date`, `order_id`, `product`, `category`, `region`, `quantity`, `unit_price`, `total_amount`); raise `FileNotFoundError` if file missing; raise `ValueError` with actionable message if columns absent or `total_amount` non-numeric
- [x] T005 [P] Implement `src/transforms.py` — define four functions per `contracts/module-contracts.md`: `compute_kpis(df)` returning `{total_sales, total_orders}`; `compute_time_series(df, granularity)` returning period+sales DataFrame sorted ascending; `compute_category_sales(df)` returning category+sales DataFrame sorted descending; `compute_region_sales(df)` returning region+sales DataFrame sorted descending

**Checkpoint**: `src/loader.py` and `src/transforms.py` exist and are importable — all story phases can now begin

---

## Phase 3: User Story 1 — KPI Overview Page (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders on the Overview page with auto file-watch reload and inline error handling

**Independent Test**: Open `http://localhost:8501` — Overview page is the default. Confirm two KPI metrics visible; values match manual CSV calculation; renaming the CSV shows an error message

### Implementation for User Story 1

- [x] T006 [US1] Scaffold `pages/1_Overview.py` — call `os.path.getmtime("data/sales-data.csv")` and `load_data("data/sales-data.csv", mtime=mtime)` inside a `try/except (FileNotFoundError, ValueError)`; on error call `st.error(str(e))` then `st.stop()`
- [x] T007 [US1] Display KPI metrics in `pages/1_Overview.py` — call `compute_kpis(df)`; render Total Sales with `st.metric("Total Sales", f"${kpis['total_sales']:,.0f}")` and Total Orders with `st.metric("Total Orders", f"{kpis['total_orders']:,}")` in a two-column layout via `st.columns(2)`

### Tests for User Story 1 (after implementation)

- [x] T008 [P] [US1] Write unit tests for `compute_kpis()` in `tests/unit/test_transforms.py` — test correct sum of `total_amount`, correct row count, empty DataFrame returns zeros
- [x] T009 [P] [US1] Write unit tests for `load_data()` in `tests/unit/test_loader.py` — test `FileNotFoundError` on missing path, `ValueError` on missing columns, `ValueError` on non-numeric `total_amount`, successful load returns correct dtypes

**Checkpoint**: User Story 1 fully functional and testable independently — run `pytest tests/unit/` to confirm

---

## Phase 4: User Story 2 — Sales Trend Page (Priority: P2)

**Goal**: Line chart with daily/monthly toggle, defaulting to monthly on first load

**Independent Test**: Navigate to Sales Trend page. Chart renders with monthly data by default; switching to Daily updates chart instantly; hover tooltip shows date + value

### Implementation for User Story 2

- [ ] T010 [US2] Scaffold `pages/2_Sales_Trend.py` — call `os.path.getmtime` and `load_data` with the same inline `try/except` error pattern as `pages/1_Overview.py`
- [ ] T011 [US2] Add granularity toggle and line chart in `pages/2_Sales_Trend.py` — render `st.radio("Granularity", ["Monthly", "Daily"], index=0)` to capture user selection; map selection to `"monthly"` or `"daily"`; call `compute_time_series(df, granularity)`; render with `plotly.express.line(ts_df, x="period", y="sales", title="Sales Trend")`; display via `st.plotly_chart(fig, use_container_width=True)`

### Tests for User Story 2 (after implementation)

- [ ] T012 [P] [US2] Write unit tests for `compute_time_series()` in `tests/unit/test_transforms.py` — test daily grouping produces one row per day, monthly grouping produces one row per month, output sorted ascending by period, raises `ValueError` for invalid granularity

**Checkpoint**: User Stories 1 AND 2 both work independently — `pytest tests/unit/` passes

---

## Phase 5: User Story 3 — Category & Regional Breakdowns Page (Priority: P3)

**Goal**: Two sorted bar charts (Sales by Category, Sales by Region) on a single Breakdowns page

**Independent Test**: Navigate to Breakdowns page. Two bar charts visible; all 5 categories and 4 regions shown; bars sorted highest-to-lowest; hover tooltip shows name + value

### Implementation for User Story 3

- [ ] T013 [US3] Scaffold `pages/3_Breakdowns.py` — call `os.path.getmtime` and `load_data` with the same inline `try/except` error pattern as previous pages
- [ ] T014 [US3] Implement Sales by Category chart in `pages/3_Breakdowns.py` — call `compute_category_sales(df)`; render with `plotly.express.bar(cat_df, x="category", y="sales", title="Sales by Category")`; display via `st.plotly_chart(fig, use_container_width=True)`
- [ ] T015 [US3] Implement Sales by Region chart in `pages/3_Breakdowns.py` — call `compute_region_sales(df)`; render with `plotly.express.bar(reg_df, x="region", y="sales", title="Sales by Region")`; display via `st.plotly_chart(fig, use_container_width=True)`

### Tests for User Story 3 (after implementation)

- [ ] T016 [P] [US3] Write unit tests for `compute_category_sales()` and `compute_region_sales()` in `tests/unit/test_transforms.py` — test output sorted descending, all input categories/regions present in output, correct sales totals per group

**Checkpoint**: All three user stories independently functional — `pytest tests/unit/` passes

---

## Phase 6: Polish & Deployment

**Purpose**: Deploy to Streamlit Community Cloud and validate end-to-end

- [ ] T017 Deploy app to Streamlit Community Cloud — go to share.streamlit.io, connect repo `001-ecommerce-dashboard` branch (or `main` after merge), set main file to `app.py`, click Deploy; confirm build succeeds without errors
- [ ] T018 Run post-deploy validation checklist from `specs/001-ecommerce-dashboard/quickstart.md` against the live public URL — verify all Overview, Sales Trend, Breakdowns, file-watch, and error-handling items pass in the deployed environment

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — blocks all user story pages
- **User Stories (Phase 3–5)**: All depend on Phase 2 completion; can proceed in priority order P1 → P2 → P3
- **Polish (Phase 6)**: Depends on all user stories complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2 — no story dependencies
- **User Story 2 (P2)**: Can start after Phase 2 — no story dependencies
- **User Story 3 (P3)**: Can start after Phase 2 — no story dependencies

### Within Each User Story

- Scaffold (data loading task) MUST complete before chart/KPI tasks
- Tests written AFTER implementation tasks in same story phase
- Both test tasks within a story [P] can run in parallel (different test files)

### Parallel Opportunities

- T002, T003 can run in parallel (different files)
- T004, T005 can run in parallel (different modules, no cross-dependency)
- T008, T009 can run in parallel (different test files)
- T012 can run in parallel with T008/T009 (different test file)
- T016 can run in parallel with T012 (different test additions)

---

## Parallel Execution Examples

```bash
# Phase 2: Run both module implementations simultaneously
Task: "Implement src/loader.py (T004)"
Task: "Implement src/transforms.py (T005)"  # ← parallel with T004

# Phase 3: Run both unit test files simultaneously (after T006, T007)
Task: "Write tests for compute_kpis() in tests/unit/test_transforms.py (T008)"
Task: "Write tests for load_data() in tests/unit/test_loader.py (T009)"  # ← parallel with T008
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T003)
2. Complete Phase 2: Foundational (T004–T005) — **CRITICAL**
3. Complete Phase 3: User Story 1 (T006–T009)
4. **STOP and VALIDATE**: Open dashboard, confirm KPIs display correctly
5. Run `pytest tests/unit/` — all tests green

### Incremental Delivery

1. Setup + Foundational → shared modules ready
2. US1 (T006–T009) → KPI page live → **deploy preview**
3. US2 (T010–T012) → Trend page live → redeploy
4. US3 (T013–T016) → Breakdowns page live → redeploy
5. Polish (T017–T018) → production deploy + validated

---

## Notes

- `[P]` = different files, no dependencies — safe to implement concurrently
- `[Story]` label maps each task to its user story for traceability
- Error handling is **inline** in each page's scaffold task — no separate error task
- Tests are written **after** implementation within each story phase
- `data/sales-data.csv` already exists — no data generation task needed
- Commit after each checkpoint with Jira key in message (e.g., `feat: add KPI overview [ECOM-1]`)
