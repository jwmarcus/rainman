FROM python:3.11-alpine

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /app

# command to run on container start
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80" ]
