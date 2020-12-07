# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory to /app
WORKDIR /raheesapp

# Copy the current directory contents into the container at /app
COPY . /raheesapp

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "flask1.py"]