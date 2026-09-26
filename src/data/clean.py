"""Functions for cleaning and preparing data."""
import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning steps to a raw DataFrame."""
    df = df.copy()

    # Standardize column names: lowercase, underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Drop fully duplicate rows
    df = df.drop_duplicates()

    # Drop rows where all values are missing
    df = df.dropna(how="all")

    return df.reset_index(drop=True)
