# CI/CD

This section introduces continuous integration with a GitHub Actions workflow example.

## Topics

- Run checks automatically for pushes and pull requests
- Select a Python version for the job
- Keep automated tests repeatable

## Example: Python test workflow

[`tests.example.yml`](tests.example.yml) shows a workflow that runs Python's `unittest` discovery.

To activate it, copy the example to `.github/workflows/tests.yml` and add a `tests` directory containing tests. The example file is intentionally not an active workflow.

The workflow runs `python -m unittest discover -s tests` on GitHub Actions; no commit or push is required to read or adapt this example.
