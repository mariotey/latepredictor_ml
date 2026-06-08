FROM python:3.11

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy only dependency files first (for caching)
COPY pyproject.toml uv.lock ./

# Install dependencies into the container environment
ENV UV_PROJECT_ENVIRONMENT=/app/.venv
RUN uv sync --frozen

# Copy application code
COPY . .

# Ensure correct import path (only needed if using /src layout)
ENV PYTHONPATH=/app/src

# Render sets PORT automatically
CMD ["/app/.venv/bin/uvicorn", "fastapi_app.main:app", "--host", "0.0.0.0", "--port", "10000"]