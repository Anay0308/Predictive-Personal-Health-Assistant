import pandas as pd

def handle_missing_values(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """Fill missing values with mean/median/mode/zero."""
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if strategy == "mean":
                df[col].fillna(df[col].mean(), inplace=True)
            elif strategy == "median":
                df[col].fillna(df[col].median(), inplace=True)
            elif strategy == "mode":
                df[col].fillna(df[col].mode()[0], inplace=True)
            else:
                df[col].fillna(0, inplace=True)
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from the dataset."""
    return df.drop_duplicates()
