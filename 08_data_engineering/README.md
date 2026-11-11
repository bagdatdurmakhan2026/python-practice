# Data Engineering

This section demonstrates a small data-processing pipeline using Python's standard library.

## Topics

- Read tabular CSV data
- Convert string fields to numeric values
- Aggregate rows into a result

## Example: sum CSV amounts

[`csv_pipeline_example.py`](csv_pipeline_example.py) parses sample CSV data and calculates the total amount.

Run from the repository root:

```powershell
python 08_data_engineering\csv_pipeline_example.py
```

Expected output: `{'total': 13}`. The sample input is embedded in the script, so no external data file is required.

## Intermediate example: monthly transaction report

[`transaction_report_example.py`](transaction_report_example.py) streams CSV rows, validates dates and decimal amounts, and aggregates totals by month and category without using floating-point arithmetic.

```powershell
python 08_data_engineering\transaction_report_example.py
```

Malformed rows fail with their line number. Replace the embedded sample input with a file stream to process a CSV file.
