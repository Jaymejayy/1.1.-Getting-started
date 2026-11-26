
# 1.1 Getting Started - Hash Generator

A simple Python application that generates a random UUID on startup and prints it every 5 seconds with a UTC timestamp.

## First Deployment

This project demonstrates deploying a containerized Python application using Docker and Kubernetes (k3d).

## Requirements

- Python 3
- Docker
- Kubernetes
- k3d

## Run Locally

```bash
python3 app.py
```

## Build Docker Image

```bash
docker build -t hashgenerator:1.0 .
```

## Run Docker Container

```bash
docker run --name hashgenerator hashgenerator:1.0
```

## Import Image into k3d

```bash
k3d image import hashgenerator:1.0 -c k3s-default
```

## Check Kubernetes Pods

```bash
kubectl get pods
```

## View Application Logs

```bash
kubectl logs -f <pod-name>
```
<<<<<<< HEAD
# Hash Generator

A simple Python application that generates a random UUID
on startup and prints it every 5 seconds with a UTC timestamp.

## Requirements

- Python 3
- Docker

## Run locally

```bash
python3 app.py
=======
# 1.1.-Getting-started
First deployment
>>>>>>> d7a1cde31979626c49924f6201f0d3e3a1d4cd19
