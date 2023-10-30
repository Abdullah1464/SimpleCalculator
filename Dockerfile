# Use the Python image as the base image and Its advisable to specify version
FROM python:3.8 
# Set the working directory in the container
WORKDIR /app
# Copy the Python application code into the container
COPY . .
# Install the libraries specified in requirements.txt file
RUN pip install -r requirements.txt
# Expose the port where application will run
EXPOSE 8080
#command for running the application
CMD ["python", "app.py"]