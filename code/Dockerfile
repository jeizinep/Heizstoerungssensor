# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# COPY the requirements.txt into the container at /app (is here to be cached by Docker)
COPY ./requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# COPY the src
COPY ./src ./src

# Install libGL
RUN apt-get update && apt-get install -y libgl1-mesa-dev libglib2.0-0

EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]