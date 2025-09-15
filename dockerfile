FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command (for Dash / Bokeh apps)
# Change `app:server` to `main.py` for Bokeh if needed
CMD ["gunicorn", "--bind", ":$PORT", "--workers", "1", "--threads", "8", "--timeout", "0", "app:server"]
