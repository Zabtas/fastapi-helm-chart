FROM python:3.13-alpine

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Copy the application
COPY api ./api
COPY .env ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"] 