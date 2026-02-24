# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a tutorial/documentation repository ("AI-Assisted Development Workflow Tutorial") that teaches building an E-Commerce Sales Dashboard using Python, Streamlit, Pandas, and Plotly. The sample dataset is at `data/sales-data.csv`. The Streamlit app entry point is `app.py`.

### Running the app

```bash
source .venv/bin/activate
streamlit run app.py --server.headless true --server.port 8501
```

The dashboard will be available at `http://localhost:8501`.

### Linting

```bash
source .venv/bin/activate
ruff check app.py
ruff format --check app.py
```

### Key caveats

- The VM requires `python3.12-venv` system package to create virtual environments (`sudo apt-get install -y python3.12-venv`). The update script handles venv creation automatically.
- No test suite exists in this repo. Validation is done manually by running the Streamlit app and verifying the dashboard displays KPIs, trend chart, category chart, and region chart correctly.
- The `.gitignore` already covers `.venv/`, `__pycache__/`, and `.streamlit/secrets.toml`.
