#FROM ubuntu:latest
#LABEL authors="root"
#
#ENTRYPOINT ["top", "-b"]

FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r req.txt