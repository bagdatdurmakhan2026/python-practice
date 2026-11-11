# Application Architecture

This section explores how to separate application data from the logic that operates on it.

## Topics

- Model application concepts with data classes
- Keep business logic in focused functions
- Separate domain logic from input/output

## Example: order total

[`orders_example.py`](orders_example.py) defines an `Order` model and a separate `calculate_total` function.

Run from the repository root:

```powershell
python 03_application_architecture\orders_example.py
```

Expected output: `30.0` for an order with three items priced at `10.0` each.
