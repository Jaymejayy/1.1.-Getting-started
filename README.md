# Exercise 2.1 – Connecting Pods

## Overview

This exercise connects the **Ping-Pong** and **Log Output** applications using HTTP communication instead of sharing the Ping-Pong counter through a persistent volume.

## Applications

### Ping-Pong

The Ping-Pong application provides two HTTP endpoints:

- `GET /pingpong` – Returns the current pong count and increments it.
- `GET /pongs` – Returns the current pong count without incrementing it.

The counter is stored in application memory.

### Log Output

The Log Output application consists of two containers:

- **Log Generator** – Generates a timestamp and a random string and writes them to a shared file.
- **Log Reader** – Reads the generated log data and retrieves the current Ping-Pong count through an HTTP GET request.

The Log Reader sends a request to:

`http://ping-pong-svc:2345/pongs`

It displays the retrieved count alongside the timestamp and random string.

## Kubernetes Configuration

- Ping-Pong runs in its own Deployment and is exposed through the `ping-pong-svc` Service.
- Log Output runs in a Deployment with separate Log Generator and Log Reader containers.
- The Log Generator and Log Reader share a volume for the log file.
- The Ping-Pong application no longer shares a volume with Log Output.
- Kubernetes Service DNS allows Log Output to communicate with Ping-Pong inside the cluster.

## Testing

The applications can be accessed through the shared Ingress:

- `/` – Displays the Log Output timestamp, random string, and Ping-Pong count.
- `/pingpong` – Accesses the Ping-Pong endpoint.

Example Log Output:

```text
2026-11-26T09:00:00Z
Random string: example-uuid
Ping / Pongs: 5
```

Example Ping-Pong response:

```text
pong 5
```

## Result

The
