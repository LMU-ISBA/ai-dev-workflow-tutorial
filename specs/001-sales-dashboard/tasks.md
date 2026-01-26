# Tasks: E-Commerce Analytics Sales Dashboard

**Input**: Design documents from `/specs/001-sales-dashboard/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md

**Tests**: Manual testing only (per constitution - no automated tests for Phase 1)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

Single-file Streamlit application at repository root:
- `app.py` - Main application (all dashboard logic)
- `data/sales-data.csv` - Source data (already exists)
- `requirements.txt` - Dependencies
- `.gitignore` - Git ignore rules
- `README.md` - Documentation

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Initialize Python project with required dependencies and configuration

- [x] T001 Create requirements.txt with pinned dependencies (streamlit>=1.28.0, pandas>=2.0.0, plotly>=5.18.0) in requirements.txt
- [x] T002 [P] Create .gitignore with venv/, __pycache__/, .DS_Store entries in .gitignore
- [x] T003 [P] Create README.md with project title and basic description in README.md
- [x] T004 Create app.py skeleton with imports and main title in app.py

**Checkpoint**: Project structure ready - can run `streamlit run app.py` showing empty dashboard

---

## Phase 2: Foundational (Data Loading Infrastructure)

**Purpose**: Implement CSV data loading with error handling - MUST complete before ANY user story

**⚠️ CRITICAL**: No visualization work can begin until data loading is working

- [x] T005 Implement load_data() function with CSV reading and date parsing in app.py
- [x] T006 Add try-except error handling for missing/invalid CSV file in app.py
- [x] T007 Add data validation to handle empty datasets gracefully in app.py
- [x] T008 Add @st.cache_data decorator to load_data() for performance in app.py
- [x] T009 Verify data loads correctly by displaying raw DataFrame shape temporarily in app.py

**Checkpoint**: Data loads successfully with `streamlit run app.py` - shows data shape or error message

---

## Phase 3: User Story 1 - View KPIs at a Glance (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders as prominent KPI cards so finance managers can quickly assess business performance

**Independent Test**: Load dashboard and verify Total Sales (~$650,000-$700,000) and Total Orders (482) are displayed with proper formatting

### Implementation for User Story 1

- [x] T010 [US1] Calculate total_sales as sum of total_amount column in app.py
- [x] T011 [US1] Calculate total_orders as count of order_id column in app.py
- [x] T012 [US1] Create KPI display section with st.columns(2) layout in app.py
- [x] T013 [US1] Display Total Sales using st.metric() with currency formatting ($X,XXX,XXX.XX) in app.py
- [x] T014 [US1] Display Total Orders using st.metric() with number formatting in app.py
- [x] T015 [US1] Verify KPI values match expected data (Total Sales ~$650k-$700k, Total Orders 482) in app.py

**Checkpoint**: User Story 1 complete - KPIs display correctly and match data source calculations

---

## Phase 4: User Story 2 - Analyze Sales Trends Over Time (Priority: P2)

**Goal**: Display a line chart showing monthly sales trends so executives can understand business growth patterns

**Independent Test**: Load dashboard and verify line chart shows 12 months of data with interactive tooltips displaying exact values

### Implementation for User Story 2

- [x] T016 [US2] Create monthly_sales aggregation using Pandas groupby on date column in app.py
- [x] T017 [US2] Convert date to month period for proper time series grouping in app.py
- [x] T018 [US2] Create Plotly line chart with px.line() for sales trend in app.py
- [x] T019 [US2] Configure X-axis as Month with proper date formatting in app.py
- [x] T020 [US2] Configure Y-axis as Sales Amount with currency formatting in app.py
- [x] T021 [US2] Add interactive tooltips showing month and exact sales value in app.py
- [x] T022 [US2] Add clear chart title "Sales Trend Over Time" in app.py
- [x] T023 [US2] Display chart using st.plotly_chart() with use_container_width=True in app.py

**Checkpoint**: User Story 2 complete - Line chart displays monthly trends with tooltips

---

## Phase 5: User Story 3 - Understand Sales by Category (Priority: P3)

**Goal**: Display a bar chart showing sales by product category so marketing directors can allocate budget effectively

**Independent Test**: Load dashboard and verify bar chart shows 5 categories (Electronics, Accessories, Audio, Wearables, Smart Home) sorted by value with tooltips

### Implementation for User Story 3

- [ ] T024 [US3] Create category_sales aggregation using Pandas groupby on category column in app.py
- [ ] T025 [US3] Sort category aggregation by total sales descending in app.py
- [ ] T026 [US3] Create Plotly horizontal bar chart with px.bar() for category breakdown in app.py
- [ ] T027 [US3] Configure chart with category on Y-axis and sales on X-axis in app.py
- [ ] T028 [US3] Add interactive tooltips showing category name and exact sales value in app.py
- [ ] T029 [US3] Add clear chart title "Sales by Product Category" in app.py

**Checkpoint**: User Story 3 complete - Category bar chart displays with correct sorting and tooltips

---

## Phase 6: User Story 4 - Understand Sales by Region (Priority: P4)

**Goal**: Display a bar chart showing sales by geographic region so regional managers can identify territory performance

**Independent Test**: Load dashboard and verify bar chart shows 4 regions (North, South, East, West) sorted by value with tooltips

### Implementation for User Story 4

- [ ] T030 [US4] Create region_sales aggregation using Pandas groupby on region column in app.py
- [ ] T031 [US4] Sort region aggregation by total sales descending in app.py
- [ ] T032 [US4] Create Plotly horizontal bar chart with px.bar() for region breakdown in app.py
- [ ] T033 [US4] Configure chart with region on Y-axis and sales on X-axis in app.py
- [ ] T034 [US4] Add interactive tooltips showing region name and exact sales value in app.py
- [ ] T035 [US4] Add clear chart title "Sales by Region" in app.py

**Checkpoint**: User Story 4 complete - Region bar chart displays with correct sorting and tooltips

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Professional styling, layout refinement, and deployment preparation

- [ ] T036 Add dashboard main title "ShopSmart Sales Dashboard" using st.title() in app.py
- [ ] T037 Arrange Category and Region charts side-by-side using st.columns(2) in app.py
- [ ] T038 Add consistent color scheme across all Plotly charts in app.py
- [ ] T039 Add section headers/dividers between KPIs, trend chart, and breakdown charts in app.py
- [ ] T040 Verify all edge cases: empty data shows appropriate messages in app.py
- [ ] T041 Update README.md with setup instructions and feature description in README.md
- [ ] T042 Run quickstart.md verification checklist manually
- [ ] T043 Deploy to Streamlit Community Cloud and verify public URL access

**Checkpoint**: Dashboard complete - Professional appearance, all features working, deployed to cloud

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational - Can start after data loading works
- **User Story 2 (Phase 4)**: Depends on Foundational - Can run parallel to US1
- **User Story 3 (Phase 5)**: Depends on Foundational - Can run parallel to US1/US2
- **User Story 4 (Phase 6)**: Depends on Foundational - Can run parallel to US1/US2/US3
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational - No dependencies on other stories

### Within Each User Story

Since this is a single-file application, tasks within each story should be completed sequentially:
1. Data aggregation first
2. Chart creation second
3. Styling/formatting third

### Parallel Opportunities

- T002 and T003 can run in parallel (different files)
- After Foundational phase, all four user stories can theoretically be developed in parallel (though they all modify app.py)
- In practice, sequential development recommended for single-file architecture

---

## Parallel Example: Setup Phase

```bash
# These can run in parallel (different files):
Task: "Create .gitignore with venv/, __pycache__/, .DS_Store entries in .gitignore"
Task: "Create README.md with project title and basic description in README.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T009)
3. Complete Phase 3: User Story 1 (T010-T015)
4. **STOP and VALIDATE**: Verify KPIs display correctly
5. Demo to stakeholders - this alone delivers core value

### Incremental Delivery

1. Complete Setup + Foundational → Data loading works
2. Add User Story 1 → KPIs visible → **MVP Ready!**
3. Add User Story 2 → Trend chart visible → Demo update
4. Add User Story 3 → Category chart visible → Demo update
5. Add User Story 4 → Region chart visible → Demo update
6. Complete Polish → Professional appearance → Final deploy

### Single Developer Strategy (Recommended)

Since this is a single-file application:
1. Complete all setup and foundational tasks first
2. Implement user stories sequentially (P1 → P2 → P3 → P4)
3. Polish and deploy last
4. Commit after each user story completion

---

## Notes

- All visualization code is in single file (app.py) per constitution Principle IV
- Manual testing only - verify against quickstart.md checklist
- Commit with Jira keys (e.g., `ECOM-1: add KPI cards`)
- Each checkpoint should result in a working dashboard state
- Total tasks: 43
- Estimated complexity: Low (single-file, well-defined requirements)
