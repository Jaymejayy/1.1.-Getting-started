# Exercise 1.12 – The Project

## Overview

This exercise adds a random image to the Todo application using [Lorem Picsum](https://picsum.photos/1200).

The application displays an image on its homepage and caches the downloaded image for 10 minutes.

## How It Works

1. When the application receives a request for an image, it checks whether a cached image exists.
2. If no cached image exists, it downloads a random image from `https://picsum.photos/1200`.
3. The downloaded image is saved as `/app/cache/image.jpg`.
4. The cached image is reused for requests made within 10 minutes.
5. After 10 minutes, the next request attempts to download a new image.
6. If downloading a new image fails, the application continues serving the existing cached image when available.

## Persistent Storage

A PersistentVolume and PersistentVolumeClaim are used to store the cached image.

The Todo application mounts the PVC at:

```text
/app/cache
```

This ensures that the cached image remains available even when the application container restarts.

## Docker Image

The updated application image is:

```text
todo-app:3.0
```

## Testing

The following tests were performed:

- Verified that the Todo application displays a random image.
- Restarted the Todo application Deployment.
- Confirmed that the same cached image was still displayed after the restart.

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- PersistentVolume (PV)
- PersistentVolumeClaim (PVC)
- Lorem Picsum API
