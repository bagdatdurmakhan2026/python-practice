# Backend Architecture

This section introduces backend APIs, request handling, and health checks.

## Topics

- Define HTTP endpoints
- Return structured JSON responses
- Add health checks for services

## Example: FastAPI health endpoint

[`api_example.py`](api_example.py) exposes `GET /health` and returns `{"status": "ok"}`.

Install the example's dependencies if needed:

```powershell
python -m pip install fastapi uvicorn
```

Start the development server from the repository root:

```powershell
python -m uvicorn api_example:app --app-dir 04_backend_architecture --reload
```

Open `http://127.0.0.1:8000/health` to see the response. Stop the server with `Ctrl+C`.
