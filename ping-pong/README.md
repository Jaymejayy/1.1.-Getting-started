# Exercise 1.9 – Ping-Pong Application

## Description

The Ping-Pong application responds to HTTP GET requests at `/pingpong`.

Each request returns a response containing `pong` and a counter that increases with every request. The counter is stored in application memory and may reset when the application restarts.

## Application

- Framework: Flask
- Application port: 3000
- Endpoint: `/pingpong`
- Docker image: `ping-pong:1.0`

## Kubernetes Deployment

The application runs in a Kubernetes Deployment named `ping-pong-dep`.

A ClusterIP Service named `ping-pong-svc` exposes the application internally on port `2345` and forwards requests to container port `3000`.

## Ingress Routing

The Ping-Pong application shares an Ingress with the Log Output application.

| Path | Application |
|---|---|
| `/` | Log Output |
| `/pingpong` | Ping-Pong |

## Access

- Log Output: `http://localhost:8081/`
- Ping-Pong: `http://localhost:8081/pingpong`
