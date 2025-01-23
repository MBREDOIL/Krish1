FROM python:3.9.2-slim-buster
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/


RUN apt-get update && apt-get install -y \
    poppler-utils

# Verify the installation
RUN pdftoppm -v


RUN pip3 install -r requirements.txt
CMD gunicorn app:app & python3 main.py

