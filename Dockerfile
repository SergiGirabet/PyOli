FROM python:latest

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app

RUN pip3 install -r requirements.txt
ADD . /app/
RUN python3 manage.py migrate