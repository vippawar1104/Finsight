"""
Configuration management for Finsight application.
Centralizes all configuration settings and paths.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = DATA_DIR / "databases"
EXPORTS_DIR = DATA_DIR / "exports"

# Ensure directories exist
DATABASE_DIR.mkdir(parents=True, exist_ok=True)
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Database paths
USERS_DB = DATABASE_DIR / "users.db"
ADMIN_DB = DATABASE_DIR / "admin.db"

def get_user_db_path(email: str) -> Path:
    """
    Get the database path for a specific user.
    
    Args:
        email: User's email address
        
    Returns:
        Path to the user's database file
    """
    # Sanitize email for filename
    safe_email = email.replace("@", "_at_").replace(".", "_")
    return DATABASE_DIR / f"user_{safe_email}.db"

# API Configuration
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Application settings
APP_TITLE = "Finsight"
APP_DESCRIPTION = "An AI powered finance tracker."
APP_ICON = "💰"

# Streamlit configuration
STREAMLIT_CONFIG = {
    "page_title": APP_TITLE,
    "page_icon": APP_ICON,
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Categories for expenses
EXPENSE_CATEGORIES = [
    "Food & Dining",
    "Transportation",
    "Shopping",
    "Entertainment",
    "Bills & Utilities",
    "Healthcare",
    "Education",
    "Travel",
    "Other"
]

# Income sources
INCOME_SOURCES = [
    "Salary",
    "Freelance",
    "Investment",
    "Business",
    "Gift",
    "Other"
]
