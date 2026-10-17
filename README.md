# MP1 Data Pipeline

A command-line data pipeline that loads, validates, cleans, and saves tabular data. The cleaning behavior is driven entirely by a YAML configuration file, so the same code can process different datasets by changing the config rather than the Python modules.

## How It Works

The pipeline first validates that the input and config file paths exist. It then loads the input data and the configuration using a loader that selects the right parser based on file extension. Next it validates the DataFrame, confirming required columns are present and dropping rows with non-numeric values in columns that should be numeric. The validated data is then processed by removing duplicate rows, dropping rows with missing values, and filtering outliers using the IQR method, according to the settings enabled in the config. Finally, the cleaned data is saved to a CSV file and a cleaning report summarizing the changes is printed.

## Project Structure

- `pipeline.py` — coordinates the end-to-end pipeline and handles CLI arguments.
- `src/data_loaders.py` — loads CSV, JSON, and YAML files based on extension.
- `src/data_validator.py` — checks required columns exist and removes rows with invalid numeric values.
- `src/data_processor.py` — removes duplicates, handles missing values, and removes outliers.
- `src/data_output.py` — saves the cleaned DataFrame to a CSV file.
- `src/utils.py` — logging setup and input-file validation.
- `config/config.yaml` — controls validation and processing behavior.

## Usage

```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

Running the command above processes the 100-row sample dataset: validation removes 2 rows with invalid ratings (100 → 98), and processing removes duplicates, missing values, and outliers (98 → 92). The cleaned data is written to output/clean.csv, and the pipeline prints a report showing 6 total rows removed with all 5 columns preserved.
