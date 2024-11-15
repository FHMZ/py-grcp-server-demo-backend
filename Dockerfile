# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Team responsible for maintaining the project
LABEL maintainer="EasyGroupIT"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/opt/venv

# Set working directory inside the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python3 -m venv $VIRTUAL_ENV \
    && $VIRTUAL_ENV/bin/pip install --upgrade pip setuptools wheel \
    && ln -s $VIRTUAL_ENV/bin/pip /usr/local/bin/pip \
    && ln -s $VIRTUAL_ENV/bin/python /usr/local/bin/python

# Copy only requirements files to leverage Docker caching
COPY ./requirements.txt ./requirements-dev.txt ./

# Install production and development dependencies
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

# Copy the application code into the container
COPY . .

# Expose the application port
EXPOSE 50051

# Specify the command to run the application
CMD ["python", "app/app.py"]
