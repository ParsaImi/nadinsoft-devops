FROM python:3.13-slim

# Create and set the working directory in container
ENV HOME=/home/app/simple_app

RUN mkdir -p $HOME
WORKDIR $HOME

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1


# Copy the Django project to the container
COPY ./simple_app $HOME

#Upgrade pip
RUN pip install --upgrade pip

# install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

