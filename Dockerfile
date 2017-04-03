FROM python:3.6-slim

RUN mkdir /app
RUN apt-get -y update && apt-get -y install locales git-core gcc g++ netcat libxml2-dev libxslt-dev libz-dev
COPY docker-entrypoint.sh /

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
RUN python setup.py develop
