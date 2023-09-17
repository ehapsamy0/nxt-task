# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install gettext -y && apt install cron -y && apt install -y certbot python3-certbot-nginx

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Copy the current directory contents into the container at /app/
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django application using the run.sh script
COPY run.sh /run.sh
RUN chmod +x /run.sh
