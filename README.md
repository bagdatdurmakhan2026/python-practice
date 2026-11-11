# Python Practice & Engineering Roadmap

A hands-on learning repository for Python, algorithms, software engineering, and the systems used to build and operate applications. It combines practice exercises with introductory examples for backend development, deployment, data, and infrastructure.

## Repository map

| Section | What you'll find |
| --- | --- |
| [`01_python_fundamentals/`](01_python_fundamentals/README.md) | Python practice, algorithms, data structures, and fundamentals. Try the [LRU cache](01_python_fundamentals/lru_cache_example.py). |
| [`02_software_engineering/`](02_software_engineering/README.md) | Input validation and maintainable coding practices. Try the [retry policy](02_software_engineering/retry_policy_example.py). |
| [`03_application_architecture/`](03_application_architecture/README.md) | Application models and separation of business logic. Try the [order service](03_application_architecture/order_service_example.py). |
| [`04_backend_architecture/`](04_backend_architecture/README.md) | HTTP APIs and service health checks. Try the [validated notes API](04_backend_architecture/notes_api_intermediate_example.py). |
| [`05_deployment/`](05_deployment/README.md) | Environments, configuration, and deployment fundamentals. Try the [validated configuration](05_deployment/validated_config_example.py). |
| [`06_docker/`](06_docker/README.md) | Container images and application packaging. See the [multi-stage API image](06_docker/Dockerfile.production.example). |
| [`07_databases/`](07_databases/README.md) | Relational databases and SQLite. Try the [SQLite repository](07_databases/sqlite_repository_example.py). |
| [`08_data_engineering/`](08_data_engineering/README.md) | Loading, transforming, and aggregating data. Try the [monthly transaction report](08_data_engineering/transaction_report_example.py). |
| [`09_ci_cd/`](09_ci_cd/README.md) | Automated checks and continuous integration. See the [Python version matrix workflow](09_ci_cd/tests.matrix.example.yml). |
| [`10_infrastructure/`](10_infrastructure/README.md) | Infrastructure as Code concepts. See the [validated deployment contract](10_infrastructure/environment_contract.example.tf). |
| [`11_monitoring/`](11_monitoring/README.md) | Application logging and observability basics. Try [request-scoped observability](11_monitoring/request_observability_example.py). |
| [`12_system_design/`](12_system_design/README.md) | Components, responsibilities, and system request flows. Read the [intermediate notes service design](12_system_design/notes_service_intermediate_example.md). |

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
