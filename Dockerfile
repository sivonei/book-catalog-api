# Use Python base image

FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
# This assumes your Dockerfile is in the root of your project
COPY . .

# Expose port
EXPOSE 8000

# Entrypoint is defined in docker-compose
