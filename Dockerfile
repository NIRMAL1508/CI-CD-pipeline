# Use the official Python 3 image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the score.py script to the working directory
COPY score.py .

# Set the command to run the script
CMD ["python", "score.py"]
