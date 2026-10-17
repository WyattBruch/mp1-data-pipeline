"""
Data Processing Pipeline - CLI
DS 3500 - MP1
"""
import argparse
import logging
import sys

from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)

logger = logging.getLogger(__name__)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Data processing pipeline")
    parser.add_argument("--input", "-i", required=True, help="Path to the input file")
    parser.add_argument("--config", "-c", required=True, help="Path to the YAML config file")
    parser.add_argument("--output", "-o", required=True, help="Path to the output file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(
        f"Arguments parsed: input={args.input}, output={args.output}, config={args.config}"
    )

    # Validate input and config files
    if not validate_input(args.input):
        sys.exit(1)
    if not validate_input(args.config):
        sys.exit(1)

    # Load the data and configuration
    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)

    # Validate the DataFrame
    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]
    rows_before_validation = len(data)
    try:
        data = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)
    logger.info(f"Validation complete: {rows_before_validation} -> {len(data)} rows")

    # Process the data
    df_before = data.copy()
    try:
        data = process_data(data, config)
    except ValueError:
        sys.exit(1)
    report = create_cleaning_report(df_before, data)
    logger.info(f"Processing complete: {report['rows_before']} -> {report['rows_after']} rows")

    # Save the cleaned data
    save_data(data, args.output)
    logger.info(f"Saved cleaned data to {args.output}")

    # Print the cleaning report
    print(report)


if __name__ == "__main__":
    main()
