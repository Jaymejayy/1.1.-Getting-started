# Todo App – Kubernetes Project

## Overview

This project contains a Todo application deployed on Kubernetes. It consists of a frontend application and a backend service.

## Project Structure

```text
todo-app/
├── manifests/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── pvc.yaml
├── todo-backend/
│   └── manifests/
│       ├── deployment.yaml
│       └── service.yaml
├── Dockerfile
├── app.py
└── requirements.txt
```

## Kubernetes Resources

The application runs in the Kubernetes namespace `project`.

| Resource | Name |
|---|---|
| Frontend Deployment | `todo-app-dep` |
| Frontend Service | `todo-app-svc` |
| Backend Deployment | `todo-backend-dep` |
| Backend Service | `todo-backend-svc` |
| PersistentVolumeClaim | `shared-data-claim` |
| PersistentVolume | `example-pv` |

## Services

- Frontend Service: ClusterIP, port `
