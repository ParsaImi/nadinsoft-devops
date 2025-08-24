FROM python:3.13-slim

# Create and set the working directory in container
RUN mkdir /app
WORKDIR /app

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

#Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file and install dependencies
COPY requirements.txt  /app/

# install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY . /app/

# Copy requirements first for better caching
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

