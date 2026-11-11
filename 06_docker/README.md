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
