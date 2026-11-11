# Docker

This section introduces container images and running an application in an isolated container.

## Topics

- Dockerfiles and base images
- Working directories and copying application code
- Container startup commands

## Example: package the deployment demo

[`Dockerfile.example`](Dockerfile.example) packages the existing deployment fundamentals `app.py`. Build it from the repository root so its `COPY` source is available:

```powershell
docker build -f 06_docker\Dockerfile.example -t learning-api .
```

Run the image:

```powershell
docker run --rm learning-api
```

The example uses a slim Python base image and does not publish ports or create external resources.

## Intermediate example: multi-stage API image

[`Dockerfile.production.example`](Dockerfile.production.example) installs dependencies in a builder stage, runs the API as a non-root user, and includes a container health check.

Build from the repository root:

```powershell
docker build -f 06_docker\Dockerfile.production.example -t notes-api:local .
```

Run and inspect the health endpoint:

```powershell
docker run --rm -p 8000:8000 notes-api:local
```

Open `http://localhost:8000/health`. The API stores notes in memory, so they do not persist across restarts.
