FROM python:3.11-slim

# Install system dependencies
# libreoffice-writer: for docx -> pdf
# default-jre: java runtime needed for libreoffice
RUN apt-get update && apt-get install -y \
    libreoffice-writer \
    default-jre \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy Frontend
COPY frontend /app/frontend

# Copy Backend
COPY backend /app/backend

# Set working directory to backend so paths are relative as expected
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Expose port (Documentation only, Azure uses WEBSITES_PORT)
EXPOSE 8000

# Copy startup script and fix line endings (CRLF -> LF)
COPY startup.sh /app/startup.sh
RUN sed -i 's/\r$//' /app/startup.sh && chmod +x /app/startup.sh

# Run the application via startup script
CMD ["python", "-m", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]