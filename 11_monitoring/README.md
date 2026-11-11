# Monitoring

This section introduces application logging as a first step toward observability.

## Topics

- Record application lifecycle events
- Choose a log level
- Send diagnostic output to the console

## Example: startup logs

[`logging_example.py`](logging_example.py) configures the standard Python logger and records startup and status messages.

Run from the repository root:

```powershell
python 11_monitoring\logging_example.py
```

The example uses only the Python standard library and writes its log messages to the console.
