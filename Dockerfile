# Step 1: Lightweight Python base image
FROM python:3.11-slim as production

# Step 2: Set environmental hardening flags
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Step 3: Create non-root system user for enterprise container security (Preventing container breakout attack)
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /code

# Step 4: Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Step 5: Copy code and assign ownership to non-root user
COPY ./app /code/app
RUN chown -R appuser:appuser /code

# Step 6: Drop root privileges immediately
USER appuser

EXPOSE 8080

# Step 7: Run uvicorn with connection timeout tuning and multiple worker processes
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "2", "--timeout-keep-alive", "65"]

