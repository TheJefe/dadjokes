# Use an official Python runtime as a parent image
FROM python:3.5-slim

EXPOSE 8000

# Set the working directory to /app
WORKDIR /app

ADD dadjokes /app/dadjokes
ADD manage.py /app
ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]