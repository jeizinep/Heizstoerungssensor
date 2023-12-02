# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install libGL
RUN apt-get update && apt-get install -y libgl1-mesa-dev libglib2.0-0

EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]