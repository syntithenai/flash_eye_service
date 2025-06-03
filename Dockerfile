# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your Python script into the container
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port 5021
EXPOSE 5021

# Run the app
CMD ["python", "app.py"]

