FROM python:3.13-slim

WORKDIR /app

# Install uv (single method)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy the rest of the app
COPY . .

CMD ["uv", "run", "main.py"]
