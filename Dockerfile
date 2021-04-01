FROM python:2-jessie
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./multi_celery /app
