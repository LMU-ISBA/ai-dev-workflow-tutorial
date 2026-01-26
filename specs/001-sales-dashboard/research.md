# Research: E-Commerce Analytics Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-25
**Status**: Complete

## Overview

This document captures research findings and technical decisions for the sales dashboard implementation. All technical context questions have been resolved.

---

## Decision 1: Dashboard Framework

**Question**: Which framework best meets the requirements for rapid development, interactive visualizations, and cloud deployment?

**Decision**: Streamlit

**Rationale**:
- Python-native framework aligns with team skills and constitution requirements
- Built-in widgets for KPI display (`st.metric`)
- Native Plotly integration for interactive charts
- Free cloud deployment via Streamlit Community Cloud
- Zero frontend (HTML/CSS/JS) knowledge required
- Rapid development cycle with hot reload

**Alternatives Considered**:

| Alternative | Rejected Because |
|-------------|------------------|
| Dash (Plotly) | More complex setup, requires explicit callback definitions |
| Flask + Jinja | Requires HTML/CSS knowledge, no built-in visualization |
| Panel | Smaller community, fewer deployment options |
| Gradio | Focused on ML demos, not business dashboards |

---

## Decision 2: Visualization Library

**Question**: Which charting library provides the best balance of interactivity and ease of use?

**Decision**: Plotly Express (via `plotly.express`)

**Rationale**:
- Interactive by default (hover tooltips, zoom, pan)
- Concise API - charts in 1-2 lines of code
- Consistent professional styling
- Excellent documentation and community support
- Native Streamlit integration via `st.plotly_chart()`

**Alternatives Considered**:

| Alternative | Rejected Because |
|-------------|------------------|
| Matplotlib | Static by default, requires additional work for interactivity |
| Altair | Good but less intuitive for simple charts |
| Streamlit native charts | Limited customization options |
| Bokeh | More complex API for similar results |

---

## Decision 3: Data Processing Approach

**Question**: How should data aggregation and transformation be handled?

**Decision**: Pandas with in-memory processing

**Rationale**:
- Industry standard for Python data manipulation
- Efficient groupby operations for category/region aggregation
- Built-in date parsing and time series support
- Sufficient performance for ~500 records
- Direct compatibility with Plotly Express

**Implementation Patterns**:
```python
# Monthly aggregation
df['month'] = pd.to_datetime(df['date']).dt.to_period('M')
monthly_sales = df.groupby('month')['total_amount'].sum()

# Category aggregation with sorting
category_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)

# Region aggregation with sorting
region_sales = df.groupby('region')['total_amount'].sum().sort_values(ascending=False)
```

---

## Decision 4: Error Handling Strategy

**Question**: How should the dashboard handle missing files, empty data, or malformed records?

**Decision**: Graceful degradation with user-friendly messages

**Rationale**:
- Non-technical users need clear, actionable error messages
- Dashboard should never crash with a Python traceback
- Partial functionality is better than complete failure

**Implementation Approach**:

| Scenario | Behavior |
|----------|----------|
| CSV file missing | Show `st.error()` with clear message about data file location |
| CSV file empty | Show zero KPIs, empty charts with "No data available" message |
| Malformed rows | Skip invalid rows, process valid data, optionally log warnings |
| Date parse failure | Use flexible date parsing with `pd.to_datetime(errors='coerce')` |

---

## Decision 5: Currency Formatting

**Question**: How should monetary values be displayed for US-based business?

**Decision**: US Dollar format with thousands separators

**Rationale**:
- ShopSmart is US-based e-commerce
- Consistent with PRD examples ($X,XXX,XXX)
- Standard business presentation format

**Implementation**:
```python
# For KPI display
formatted_sales = f"${total_sales:,.2f}"

# For Plotly chart tooltips
fig.update_traces(hovertemplate='$%{y:,.2f}')
```

---

## Decision 6: Chart Styling

**Question**: What styling approach ensures professional appearance suitable for executive presentations?

**Decision**: Minimal, clean Plotly defaults with consistent color scheme

**Rationale**:
- Constitution Principle II requires professional appearance
- Consistency across all charts improves readability
- Avoid over-styling that distracts from data

**Styling Guidelines**:
- Clear chart titles (descriptive, not clever)
- Axis labels with units where appropriate
- Consistent color palette across charts
- White/light background for clarity
- Adequate spacing and margins

---

## Decision 7: File Architecture

**Question**: Should the dashboard be split into multiple Python files?

**Decision**: Single file (`app.py`)

**Rationale**:
- Constitution Principle IV (Minimal Viable Solution)
- Dashboard logic is straightforward (~150-200 lines)
- No repeated patterns requiring abstraction
- Easier for students to understand and modify
- Simpler deployment (single entry point)

**When to Split**: Only if the file exceeds ~300 lines or clear module boundaries emerge (neither expected for Phase 1).

---

## Decision 8: Deployment Configuration

**Question**: What configuration is needed for Streamlit Community Cloud deployment?

**Decision**: Minimal configuration with requirements.txt

**Rationale**:
- Streamlit Cloud auto-detects `requirements.txt`
- No additional config files needed for basic deployment
- Public URL generated automatically

**Deployment Checklist**:
1. Push code to GitHub repository
2. Connect repository to Streamlit Community Cloud
3. Select `app.py` as main file
4. Deploy - URL generated automatically

---

## Performance Considerations

**Data Size**: ~500 records, <1MB CSV file
**Expected Load Time**: <2 seconds for data processing
**Expected Render Time**: <1 second per chart

**Optimization Not Needed**: The data volume is small enough that caching (`@st.cache_data`) is optional but recommended for best practice.

---

## Summary

All technical decisions align with the project constitution and PRD requirements. The chosen stack (Streamlit + Pandas + Plotly) is well-suited for rapid dashboard development with professional results.

| Category | Decision |
|----------|----------|
| Framework | Streamlit |
| Visualization | Plotly Express |
| Data Processing | Pandas (in-memory) |
| Error Handling | Graceful degradation |
| Currency Format | US Dollar ($X,XXX.XX) |
| Chart Style | Clean, minimal, consistent |
| Architecture | Single file (app.py) |
| Deployment | Streamlit Community Cloud |
