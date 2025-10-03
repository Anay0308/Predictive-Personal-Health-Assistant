import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def standardize(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Apply standardization (z-score scaling)."""
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df

def normalize(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Apply MinMax scaling to selected columns."""
    scaler = MinMaxScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df
