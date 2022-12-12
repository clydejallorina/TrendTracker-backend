# Dockerfile

# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /web/
WORKDIR /web/

# Copy requirements.txt to container
ADD requirements.txt /web/

# Install dependencies
RUN pip install -r /web/requirements.txt

# Ensure that gunicorn log directories exist
RUN mkdir -p /var/log/gunicorn/
RUN mkdir -p /var/run/gunicorn/

# Copy project to container
ADD ./TrendTracker/ /web/

# Make sure wait-for works
RUN apt-get update
RUN apt-get install -y net-tools netcat
COPY ./wait-for /web/wait-for
RUN chmod +x /web/wait-for && \
    mv /web/wait-for /bin/wait-for
