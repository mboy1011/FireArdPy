# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /fireardpy
WORKDIR /fireardpy

# Copy the current directory contents into the container at /fireardpy
COPY . /fireardpy

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME FireArdPy

# Run app.py when the container launches
CMD ["python", "fireArd.py"]

