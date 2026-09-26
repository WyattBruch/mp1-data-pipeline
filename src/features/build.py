"""Functions for building features from cleaned data."""
import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create derived features from a cleaned DataFrame."""
    df = df.copy()

    # Example: extract parts from a date column, if present
    for col in df.select_dtypes(include=["datetime64"]).columns:
        df[f"{col}_year"] = df[col].dt.year
        df[f"{col}_month"] = df[col].dt.month
        df[f"{col}_dayofweek"] = df[col].dt.dayofweek

    return df
