FROM ubuntu:latest
LABEL Maintainer="Josh Ruggles"
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/app/src
COPY files/* .
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "./collector.py"]