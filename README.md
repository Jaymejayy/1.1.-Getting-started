# Exercise 1.13 – The Project, Step 7

## Overview

This exercise adds the initial Todo application functionality to the existing project.

The application displays a Todo input field, a Send button, and a list of existing todos.

## Features

### 1. Todo Input
- Provides a text input field for entering todos.
- Limits input to a maximum of 140 characters using the HTML `maxlength` attribute.

### 2. Send Button
- Provides a Send button next to the input field.
- The button is not yet connected to any functionality.

### 3. Todo List
The application displays three hardcoded todos:

- Learn Kubernetes
- Complete the DevOps course
- Build a Todo application

### 4. Random Image
Retains the random image functionality from Exercise 1.12:
- Fetches images from Lorem Picsum.
- Caches images for 10 minutes.
- Stores cached images in persistent storage.
- Preserves the cached image across container restarts.

## Docker Image

The updated application image is:

```text
todo-app:4.
