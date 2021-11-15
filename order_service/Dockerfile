# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# edit the 3 environment variables and inform Docker that the container listens on 15004 at runtime
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=15004
EXPOSE 15004

# Run app.py when the container launches
CMD ["flask", "run"]