# Use Python 3.10 Alpine as base image
FROM public.ecr.aws/docker/library/python:3.10-alpine

# Set environment variable FLASK_RUN_HOST
ENV FLASK_RUN_HOST=0.0.0.0

# Set working directory
WORKDIR /

# Create user 'app' with UID 1000
RUN adduser -u 1000 -D app

# Install necessary packages
RUN apk update && \
    apk add \
    pcre \
    pcre-dev \
    build-base \
    gcc \
    linux-headers \
    openssl \
    libffi-dev \
    && pip install pipenv

# Create directories for the application
RUN mkdir -p /var/www/app && \
    mkdir /app

# Copy Pipfile* into the container
COPY Pipfile* /app

# Install Python packages from Pipfile.lock
RUN cd /app && pipenv install --system --deploy

# Copy all files and directories into the container
COPY . /app

# Default command when the container is started
CMD uwsgi --http :5000 --master --enable-threads -s /var/www/app/app.sock --manage-script-name --mount /=app:app
