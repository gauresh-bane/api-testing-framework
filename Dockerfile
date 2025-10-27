FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY app/ /app/app/
COPY core/ /app/core/
COPY cotils/ /app/utils/
COPY config/ /app/config/
COPY data/ /app/data/
COPY tests/ /app/tests/
COPY conftest.py pytest.ini /app/

# Expose port
EXPOSE 8000

# Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]