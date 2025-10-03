import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Load dataset from CSV file."""
    return pd.read_csv(path)

def load_excel(path: str, sheet_name: str = None) -> pd.DataFrame:
    """Load dataset from Excel file."""
    return pd.read_excel(path, sheet_name=sheet_name)

def load_json(path: str) -> pd.DataFrame:
    """Load dataset from JSON file."""
    return pd.read_json(path)
