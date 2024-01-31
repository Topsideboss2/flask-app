# Choose the Image which has flask already
FROM python:3.9-slim-buster

# make the 'app' folder the current working directory
WORKDIR /app

# copy the contents of the current directory to this location
COPY ./requirements.txt ./

# install project dependencies
RUN pip install -r requirements.txt

# copy project files and folders to the current working directory (i.e. 'intsp' folder)
COPY . .

# Expose port 5000 to the Docker host, so we can access it
EXPOSE 5000

# set environment variables
ENV FLASK_APP=main.py

# specifies the command to run when the Docker image is started 
CMD ["flask", "run", "--host", "0.0.0.0"]