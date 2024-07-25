# Pull Base Image
FROM python:3.10.4-slim-bullseye

# Set Environment Variables
ENV PIP_DISABLED_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set Working Directory
WORKDIR /code

# Install Dependencies
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy Project
COPY . .
