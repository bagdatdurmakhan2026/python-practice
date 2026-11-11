# Software Engineering

This section practices small engineering techniques that make code safer and easier to maintain.

## Topics

- Validate inputs at system boundaries
- Normalize data consistently
- Raise clear errors for invalid values
- Keep functions focused and predictable

## Example: username validation

[`username_example.py`](username_example.py) trims whitespace, converts a username to lowercase, and rejects values shorter than three characters.

Run from the repository root:

```powershell
python 02_software_engineering\username_example.py
```

Expected output: `alex`. Try changing the input to a one- or two-character value to see the validation error.

## Intermediate example: retry policy

[`retry_policy_example.py`](retry_policy_example.py) retries only explicitly selected exception types, applies exponential backoff, and accepts an injected sleep function so retry behavior can be tested without waiting.

```powershell
python 02_software_engineering\retry_policy_example.py
```

The example simulates two temporary connection failures and then succeeds. Avoid retrying non-idempotent operations unless they have an idempotency strategy.
