"""Main analysis pipeline: load, clean, build features, summarize."""
from pathlib import Path
import pandas as pd

from src.data.load import load_config, load_raw
from src.data.clean import clean_data
from src.features.build import add_features


def run(filename: str) -> pd.DataFrame:
    """Run the full pipeline on a raw data file and return the result."""
    config = load_config()
    df = load_raw(filename, config)
    df = clean_data(df)
    df = add_features(df)
    return df


def main():
    config = load_config()
    # Replace with your actual raw data filename
    df = run("your_file.csv")

    print("Shape:", df.shape)
    print("\nSummary statistics:")
    print(df.describe())

    # Save processed output
    out_dir = Path(config["data"]["processed_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_dir / "processed.csv", index=False)
    print(f"\nSaved processed data to {out_dir / 'processed.csv'}")


if __name__ == "__main__":
    main()
