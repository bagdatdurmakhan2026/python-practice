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
