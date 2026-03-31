---
description: "Task list for ShopSmart Sales Analytics Dashboard"
---

# Tasks: ShopSmart Sales Analytics Dashboard

**Input**: Design documents from `specs/001-analytics-dashboard/`
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, quickstart.md ✅

**Tests**: Not requested — validation via `quickstart.md` checklist instead.

**Organization**: Tasks are grouped by user story to enable independent implementation
and testing of each story.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Exact file paths included in all descriptions

---

## Phase 1: Setup

**Purpose**: Project initialization — reproducible environment before any code is written.

- [x] T001 Create `requirements.txt` at repo root with pinned versions: `streamlit==1.32.0`, `pandas==2.2.3`, `plotly>=5.0.0`, `numpy==1.26.4`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared infrastructure that ALL user stories depend on. MUST complete before
any story work begins.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T002 Create `data.py` at repo root with `load_data()`: reads `data/sales-data.csv` using pandas, applies `@st.cache_data`, excludes rows with null/non-numeric `total_amount`, and raises a descriptive error if the file is missing or unreadable
- [x] T003 Create `app.py` at repo root with Streamlit page config: set page title to "ShopSmart Sales Dashboard", wide layout, and a call to `load_data()` from `data.py`

**Checkpoint**: `streamlit run app.py` runs without errors and loads the CSV. Foundation ready.

---

## Phase 3: User Story 1 — KPI Scorecards (Priority: P1) 🎯 MVP

**Goal**: Finance manager sees Total Sales and Total Orders as clean metric cards on page load.

**Independent Test**: Run `streamlit run app.py` → confirm two metric cards appear showing
~$650K–$700K total sales and 482 total orders with no other interaction required.

- [x] T004 [US1] Add `get_kpis(df)` to `data.py`: returns `{"total_sales": float, "total_orders": int}` computed from the loaded DataFrame
- [x] T005 [US1] Add KPI scorecard layout to `app.py`: two `st.columns(2)` with `st.metric()` cards — "Total Sales" (currency-formatted, e.g. `$672,345`) and "Total Orders" (integer with comma separator)

**Checkpoint**: US1 fully functional. An executive can see both KPIs at a glance. ✅ MVP.

---

## Phase 4: User Story 2 — Sales Trend Chart (Priority: P2)

**Goal**: CEO sees monthly sales totals as a line chart with 12 data points (Jan–Dec 2024).

**Independent Test**: Run `streamlit run app.py` → confirm a line chart appears below KPI
cards with 12 labeled monthly points; hover over any point to verify tooltip shows exact value.

- [x] T006 [US2] Add `get_monthly_trend(df)` to `data.py`: aggregates `total_amount` by calendar month (YYYY-MM), returns a DataFrame with columns `["month", "sales"]` sorted ascending, all 12 months present
- [x] T007 [US2] Add monthly trend line chart to `app.py` below KPI cards: full-width `st.plotly_chart` using `plotly.express.line`, x-axis labeled "Month", y-axis labeled "Sales ($)", chart title "Sales Trend"

**Checkpoint**: US1 + US2 both independently functional.

---

## Phase 5: User Story 3 — Category & Region Breakdowns (Priority: P3)

**Goal**: Marketing director and regional manager see sales by category and region as
side-by-side sorted bar charts.

**Independent Test**: Run `streamlit run app.py` → confirm two bar charts appear side by
side; category chart has 5 bars sorted descending; region chart has 4 bars sorted
descending; hovering any bar shows exact sales value.

- [x] T008 [P] [US3] Add `get_category_breakdown(df)` and `get_region_breakdown(df)` to `data.py`: each aggregates `total_amount` by its dimension, returns a DataFrame with columns `["category"/"region", "sales"]` sorted descending by sales, all known values present
- [x] T009 [US3] Add side-by-side bar charts to `app.py` below the trend chart: `st.columns(2)` — left column: `plotly.express.bar` of category breakdown (title "Sales by Category"); right column: `plotly.express.bar` of region breakdown (title "Sales by Region"); both use `use_container_width=True`

**Checkpoint**: All three user stories functional end-to-end.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and deployment.

- [ ] T010 Run through every item in `specs/001-analytics-dashboard/quickstart.md` validation checklist; fix any discrepancies between displayed values and expected values from `data/sales-data.csv`
- [ ] T011 [P] Add `@st.cache_data` to any remaining uncached data calls in `app.py` if present; verify dashboard loads within 5 seconds (SC-001)
- [ ] T012 Deploy to Streamlit Community Cloud: push branch to GitHub, merge to `main`, connect repo in Streamlit Cloud dashboard, set main file to `app.py`, verify public URL is accessible with no login required (SC-005)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — BLOCKS all user stories
- **US1 (Phase 3)**: Depends on Foundational — no dependency on US2 or US3
- **US2 (Phase 4)**: Depends on Foundational — no dependency on US1 or US3
- **US3 (Phase 5)**: Depends on Foundational — no dependency on US1 or US2
- **Polish (Phase 6)**: Depends on all desired stories being complete

### User Story Dependencies

- **US1 (P1)**: Independent after Foundational ✅
- **US2 (P2)**: Independent after Foundational ✅
- **US3 (P3)**: Independent after Foundational ✅

### Within Each User Story

- `data.py` aggregation function → `app.py` chart task (in that order)
- T008 is marked [P] because `get_category_breakdown` and `get_region_breakdown`
  operate on the same file but are independent functions

### Parallel Opportunities

- T008 can be split: write both functions simultaneously if two developers are working
- US2 and US3 can proceed in parallel once Foundational is complete (if staffed)
- T011 and T012 can run in parallel in the polish phase

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002–T003)
3. Complete Phase 3: User Story 1 (T004–T005)
4. **STOP and VALIDATE**: Two KPI cards visible, values correct → MVP complete
5. Demo to stakeholders if ready

### Incremental Delivery

1. Setup + Foundational → environment ready
2. US1 (KPI cards) → **MVP** — demo-able
3. US2 (trend chart) → adds strategic context
4. US3 (breakdowns) → adds operational insight
5. Polish + Deploy → public URL, fully validated

---

## Notes

- [P] tasks = different files or independent functions, no blocking dependencies
- [Story] label maps each task to a specific user story for traceability
- Error handling for missing/malformed CSV is built into T002 (data loading)
- No automated tests in scope — use `quickstart.md` checklist for validation
- Commit after each checkpoint using pattern: `[001] short description`
