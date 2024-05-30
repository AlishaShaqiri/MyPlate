# Use the official Python image as base
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app
COPY app.py /app/

# Expose port 5000 to allow communication to/from server
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
