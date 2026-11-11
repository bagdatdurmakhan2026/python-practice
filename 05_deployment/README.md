# Deployment

This section covers application configuration and the path from local development to production.

## Topics

- Development, staging, and production environments
- Runtime configuration through environment variables
- Differences between running locally and deploying a service

## Example: environment configuration

[`config_example.py`](config_example.py) reads `APP_ENV`, defaults to `development`, and rejects unsupported environment names.

Run from the repository root:

```powershell
python 05_deployment\config_example.py
```

To try another environment in PowerShell:

```powershell
$env:APP_ENV = "staging"
python 05_deployment\config_example.py
```

For the deployment lifecycle and process exercises, see [`01_deployment_fundamentals`](01_deployment_fundamentals/README.MD).

## Intermediate example: validated configuration

[`validated_config_example.py`](validated_config_example.py) parses environment values into an immutable configuration object, validates the environment, port, and boolean settings, and hides the API token from its representation.

```powershell
$env:APP_ENV = "staging"
$env:APP_PORT = "8080"
python 05_deployment\validated_config_example.py
```

Invalid values fail with a clear error instead of being silently accepted.
