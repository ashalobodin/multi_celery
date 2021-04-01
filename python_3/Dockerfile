FROM python:3.6-alpine
WORKDIR /app
COPY python_3/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./python_3 /app
