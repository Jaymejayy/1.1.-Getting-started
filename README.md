# 1.10 – Even More Services

## Overview

This exercise splits the Log Output application into two separate containers running inside a single Kubernetes Pod.

The containers communicate through a shared volume.

## Application Architecture

### 1. Log Generator

- Generates a random UUID when the container starts.
- Generates a UTC timestamp every 5 seconds.
- Writes the timestamp and UUID to `/app/files/log.txt`.
- Appends new entries to the file.

### 2. Log Reader

- Runs a Flask HTTP server on port 3000.
- Reads the contents of `/app/files/log.txt`.
- Returns the file contents when the user accesses the `/` endpoint.

## Shared Volume

Both containers use a Kubernetes `emptyDir` volume named `log-file`.

The volume is mounted at:

```text
/app/files
```

This allows the Log Generator to write the log file and the Log Reader to access the same file.

## Docker

Build the Docker image:

```bash
docker build -t log-output:2.0 .
```

Import the image into k3d:

```bash
k3d image import log-output:2.0 -c k3s-default
```

## Kubernetes Deployment

The Deployment `log-output-dep` contains:

- `log-generator` container
- `log-reader` container
- Shared `emptyDir` volume

Apply the Deployment:

```bash
kubectl apply -f manifests/deployment.yaml
```

## Verify the Application

Check the Pods:

```bash
kubectl get pods
```

View Log Generator output:

```bash
kubectl logs &lt;pod-name&gt; -c log-generator
```

View Log Reader output:

```bash
kubectl logs &lt;pod-name&gt; -c log-reader
```

## Access the Application

The existing Kubernetes Service and Ingress expose the Log Reader.

Open:

```text
http://localhost:8081/
```

The browser displays the timestamped UUID entries stored in the shared log file.

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- k3d
>>>>>>> d7a1cde31979626c49924f6201f0d3e3a1d4cd19
