FROM python:3.13-alpine

WORKDIR /app

# Install dependencies required for Poetry
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Configure Poetry to install dependencies system-wide (no virtualenv)
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy application code
COPY api ./api
COPY .env ./

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]