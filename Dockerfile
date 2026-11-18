# Use an official Python image
FROM python:3.12-slim

# Create an application directory
WORKDIR /app

# Copy our Python application
COPY app.py .

# Start the application
CMD ["python", "app.py"]
