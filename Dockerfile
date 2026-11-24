FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY log_generator.py .
COPY log_reader.py .

EXPOSE 3000
