# our base image
FROM python:3

# specify the port number the container should expose
EXPOSE 8000

# Install Django
RUN pip install django

# Create and set the working directory
WORKDIR /app

# Copy the Django project directory into the container
COPY learning_log /app

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
