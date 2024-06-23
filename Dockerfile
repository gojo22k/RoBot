# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies needed for Python encoding
RUN apk add --no-cache libstdc++ libffi

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run when the container starts
CMD ["python3", "-m", "Adarsh"]

docker build -t my-python-app .
docker run -it --rm my-python-app

