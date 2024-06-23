# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies needed for Python encoding and other packages
RUN apt-get update && \
    apt-get install -y libstdc++ libffi libssl-dev && \
    apt-get clean

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run when the container starts
CMD ["python3", "-m", "Adarsh"]
