# Use an official Python runtime as a parent image.
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# Make port 10000 available to the world outside this container
EXPOSE 10000

# Define environment variable
# ENV NAME Tuan

# Run app.py when the container launches
CMD ["python", "tuan.py"]