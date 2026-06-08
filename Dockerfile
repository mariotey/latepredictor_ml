FROM python:3.11

# Set working directory inside container
# All subsequent commands run from /app
WORKDIR /app

# Install uv (modern Python package/dependency manager)
# Used to install dependencies from pyproject.toml + uv.lock
RUN pip install --no-cache-dir uv

# Copy dependency definition files first (enables Docker layer caching)
# This means dependencies are only reinstalled when these files change
COPY pyproject.toml uv.lock ./

# Ensure uv creates the virtual environment inside /app/.venv
# This makes environment predictable inside Docker
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

# Install all dependencies locked in uv.lock
# --frozen ensures exact reproducible installs (no version changes)
RUN uv sync --frozen

# Copy the rest of the application code into the container
COPY . .

# Ensure Python can import modules from /app/src
ENV PYTHONPATH=/app/src

# Expose the port FastAPI will run on inside the container
EXPOSE 10000

# Start the FastAPI application using uv-managed environment
# uv run ensures correct venv + dependencies are used
CMD ["uv", "run", "uvicorn", "fastapi_app.main:app", "--host", "0.0.0.0", "--port", "10000"]