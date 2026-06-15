# Dockerized Python Application

## Description

This project uses the Python 3.12 Slim Docker image.

The application prints:

* Python version running inside the container
* Current date and time

## Files

* app.py
* Dockerfile
* requirements.txt

## Build Docker Image

```bash
docker build -t python-version-app .
```

## Run Docker Container

```bash
docker run python-version-app
```

## Sample Output

```text
Python Version: 3.12.x

Current Date and Time: 2026-06-15 18:45:20
```

## Author
Purvi Jain
