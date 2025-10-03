import pandas as pd
from data_loader import load_csv
from data_cleaning import handle_missing_values, remove_duplicates
from scaling import standardize
from split import split_data

def preprocess_pipeline(path: str, target: str):
    """End-to-end preprocessing pipeline."""
    # Load data
    df = load_csv(path)

    # Clean data
    df = handle_missing_values(df, strategy="mean")
    df = remove_duplicates(df)

    # Features and target
    X = df.drop(columns=[target])
    y = df[target]

    # Scale features
    X = standardize(X, X.columns.tolist())

    # Split
    return split_data(X, y)
