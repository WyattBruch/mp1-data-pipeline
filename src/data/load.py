"""Functions for loading raw data."""
from pathlib import Path
import pandas as pd
import yaml


def load_config(path: str = "config.yaml") -> dict:
    """Load project configuration from YAML."""
    with open(path) as f:
        return yaml.safe_load(f)


def load_raw(filename: str, config: dict | None = None) -> pd.DataFrame:
    """Load a CSV file from the raw data directory."""
    if config is None:
        config = load_config()
    raw_dir = Path(config["data"]["raw_dir"])
    return pd.read_csv(raw_dir / filename)
