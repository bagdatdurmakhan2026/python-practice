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

## Intermediate example: order service

[`order_service_example.py`](order_service_example.py) separates an application service from a repository interface, validates inventory and quantity, and persists through an in-memory adapter.

```powershell
python 03_application_architecture\order_service_example.py
```

The `OrderRepository` protocol makes it possible to replace the in-memory adapter with a database implementation without changing the order workflow.
