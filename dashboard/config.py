"""
Configuration constants for the ShopSmart Sales Dashboard.

This module contains all configurable values used throughout the application.
Per Constitution Principle I, magic numbers and hardcoded values are replaced
with named constants.
"""

# Data source configuration
DATA_PATH = "data/sales-data.csv"

# Page configuration
PAGE_TITLE = "ShopSmart Sales Dashboard"
PAGE_ICON = "📊"
PAGE_LAYOUT = "wide"

# Currency formatting
CURRENCY_FORMAT = "${:,.2f}"
NUMBER_FORMAT = "{:,}"

# Chart color scheme (professional palette)
CHART_COLORS = {
    "primary": "#1f77b4",      # Blue
    "secondary": "#ff7f0e",    # Orange
    "tertiary": "#2ca02c",     # Green
    "quaternary": "#d62728",   # Red
    "quinary": "#9467bd",      # Purple
}

# Chart color sequence for consistent styling
COLOR_SEQUENCE = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728",  # Red
    "#9467bd",  # Purple
]

# Valid data categories (for validation)
VALID_CATEGORIES = [
    "Electronics",
    "Accessories",
    "Audio",
    "Wearables",
    "Smart Home",
]

# Valid regions (for validation)
VALID_REGIONS = [
    "North",
    "South",
    "East",
    "West",
]

# Required CSV columns
REQUIRED_COLUMNS = [
    "date",
    "order_id",
    "product",
    "category",
    "region",
    "quantity",
    "unit_price",
    "total_amount",
]
