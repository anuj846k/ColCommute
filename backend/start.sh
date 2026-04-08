#!/bin/bash

# Run database migrations
echo "Running alembic migrations..."
alembic upgrade head

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn --bind :8080 --workers 1 --worker-class uvicorn.workers.UvicornWorker api.main:app
