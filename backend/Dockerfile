FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for psycopg/postgres connection
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Ensure psycopg binary is installed for database connectivity
RUN pip install --no-cache-dir "psycopg[binary]"

# Copy application code
COPY . .

# Cloud Run expects the app to listen on port 8080 by default
EXPOSE 8080

# Make startup script executable
RUN chmod +x start.sh

# Start the application via the startup script to handle migrations
CMD ["./start.sh"]
