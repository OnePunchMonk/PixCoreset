# Use official Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create writable config directories for streamlit and matplotlib
RUN mkdir -p /app/.streamlit && mkdir -p /app/.config/matplotlib

# Set environment variables to avoid permission issues
ENV STREAMLIT_CONFIG_DIR=/app/.streamlit
ENV MPLCONFIGDIR=/app/.config/matplotlib

# Expose streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
