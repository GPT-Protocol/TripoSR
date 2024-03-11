# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    pip install git+https://github.com/tatsy/torchmcubes.git

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run server.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]