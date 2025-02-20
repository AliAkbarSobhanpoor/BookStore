# base image
FROM python:3.12-slim

# enviroment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory for code
WORKDIR /code

# copy requirements.txt file to the directiry
COPY ./requirements.txt .

# install requirements to the file
RUN pip install -r requirements.txt

# copy all files in the working directory to container
COPY . .