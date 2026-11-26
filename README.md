# Exercise 2.2 – The Project, Step 8

## Overview

This exercise separates the Todo application into two parts:

- **Todo App:** Handles the HTML page, displays the todo list, accepts new todos, and serves a random picture.
- **Todo Backend:** Handles storing and retrieving todo items through HTTP requests.

## Architecture

The Todo App communicates with the Todo Backend using the Kubernetes Service `todo-backend-svc`.

The backend exposes two endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/todos` | Retrieves all todo items |
| POST | `/todos` | Creates a new todo item |

## How It Works

1. The browser requests the Todo App page.
2. The Todo App sends a GET request to the backend to retrieve todos.
3. The backend returns the todo list as JSON.
4. The Todo App displays the todos in the HTML page.
5. When a user submits a new todo, the Todo App sends a POST request to the backend.
6. The backend stores the new todo and the Todo App retrieves the updated list.

## Kubernetes Resources

The exercise uses the following Kubernetes resources:

- `todo-app-dep` – Deployment for the Todo App.
- `todo-app-svc` – Service for the Todo App.
- `todo-backend-dep` – Deployment for the Todo Backend.
- `todo-backend-svc` – Service for the Todo Backend.

## Data Storage

Todo items are stored in memory in the Todo Backend. This means the stored todos are lost if the backend application restarts.

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- HTTP GET and POST requests
- JSON
