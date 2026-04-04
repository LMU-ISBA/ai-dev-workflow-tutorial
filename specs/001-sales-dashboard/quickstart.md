# Quickstart: E-Commerce Analytics Sales Dashboard

**Feature**: 001-sales-dashboard
**Date**: 2026-01-25

## Prerequisites

- Python 3.11 or higher installed
- Git installed and configured
- GitHub account (for deployment)
- Streamlit Community Cloud account (free, for deployment)

---

## Local Development Setup

### 1. Clone and Navigate to Repository

```bash
cd ai-dev-workflow-tutorial
git checkout 001-sales-dashboard
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Data File

Ensure `data/sales-data.csv` exists and contains sales transaction data.

### 6. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`.

---

## Project Structure

```
├── app.py                 # Main Streamlit application
├── data/
│   └── sales-data.csv     # Source sales data
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## Dependencies

Create `requirements.txt` with:

```text
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.18.0
```

---

## Environment Variables

No environment variables are required for Phase 1. The dashboard reads directly from the local CSV file.

---

## Deployment to Streamlit Community Cloud

### 1. Push Code to GitHub

```bash
git add .
git commit -m "ECOM-X: add sales dashboard implementation"
git push origin 001-sales-dashboard
```

### 2. Connect to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository and branch (`001-sales-dashboard`)
5. Set main file path to `app.py`
6. Click "Deploy"

### 3. Access Your Dashboard

Streamlit will provide a public URL like:
`https://your-app-name.streamlit.app`

---

## Verification Checklist

After setup, verify:

- [ ] Dashboard loads without errors
- [ ] Total Sales KPI displays (~$650,000-$700,000)
- [ ] Total Orders KPI displays (482)
- [ ] Sales trend line chart renders with 12 months
- [ ] Category bar chart shows 5 categories (sorted)
- [ ] Region bar chart shows 4 regions (sorted)
- [ ] All tooltips display on hover

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and dependencies installed |
| CSV file not found | Verify `data/sales-data.csv` exists at correct path |
| Charts not displaying | Check browser console for errors, try hard refresh |
| Port 8501 in use | Run with `streamlit run app.py --server.port 8502` |

---

## Development Workflow

1. Make changes to `app.py`
2. Streamlit auto-reloads on file save (hot reload)
3. Test changes in browser
4. Commit with Jira key: `git commit -m "ECOM-X: description"`
5. Push to trigger deployment update
