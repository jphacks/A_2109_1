FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /service
WORKDIR /service 
COPY requirements.txt /service/
RUN pip install -r requirements.txt
COPY ./src /service/
RUN apt update -y && apt install -y default-mysql-client
