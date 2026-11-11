# Python Practice & Engineering Roadmap

A hands-on learning repository for Python, algorithms, software engineering, and the systems used to build and operate applications. It combines practice exercises with introductory examples for backend development, deployment, data, and infrastructure.

## Repository map

| Section | What you'll find |
| --- | --- |
| [`01_python_fundamentals/`](01_python_fundamentals/README.md) | Python practice, algorithms, data structures, and fundamentals. Start with [the average example](01_python_fundamentals/average_example.py). |
| [`02_software_engineering/`](02_software_engineering/README.md) | Input validation and maintainable coding practices. See [username validation](02_software_engineering/username_example.py). |
| [`03_application_architecture/`](03_application_architecture/README.md) | Application models and separation of business logic. See [the order example](03_application_architecture/orders_example.py). |
| [`04_backend_architecture/`](04_backend_architecture/README.md) | HTTP APIs and service health checks. See [the FastAPI example](04_backend_architecture/api_example.py). |
| [`05_deployment/`](05_deployment/README.md) | Environments, configuration, and deployment fundamentals. See [the environment configuration example](05_deployment/config_example.py). |
| [`06_docker/`](06_docker/README.md) | Container images and application packaging. See [the Dockerfile example](06_docker/Dockerfile.example). |
| [`07_databases/`](07_databases/README.md) | Relational databases and SQLite. See [the SQLite example](07_databases/sqlite_example.py). |
| [`08_data_engineering/`](08_data_engineering/README.md) | Loading, transforming, and aggregating data. See [the CSV pipeline example](08_data_engineering/csv_pipeline_example.py). |
| [`09_ci_cd/`](09_ci_cd/README.md) | Automated checks and continuous integration. See the [GitHub Actions workflow example](09_ci_cd/tests.example.yml). |
| [`10_infrastructure/`](10_infrastructure/README.md) | Infrastructure as Code concepts. See [the Terraform example](10_infrastructure/main.example.tf). |
| [`11_monitoring/`](11_monitoring/README.md) | Application logging and observability basics. See [the logging example](11_monitoring/logging_example.py). |
| [`12_system_design/`](12_system_design/README.md) | Components, responsibilities, and system request flows. See [the notes service design](12_system_design/notes_service_example.md). |

## Getting started

Most Python examples use only the Python standard library. From the repository root, for example:

```powershell
python 01_python_fundamentals\average_example.py
python 07_databases\sqlite_example.py
```

The backend API example requires FastAPI and Uvicorn. Docker, Terraform, and GitHub Actions examples require their respective tools; see each section's README for usage instructions. Files named `*.example.*` are learning samples and are not automatically active configurations.

## Learning approach

1. Choose a section and read its README.
2. Run the example and inspect its output.
3. Change the input or implementation and observe the result.
4. Add tests or notes as you learn.

The examples are educational starting points, not production-ready services or infrastructure.
