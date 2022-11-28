FROM python:3

WORKDIR /PIADockerizado

COPY requirements.txt /PIADockerizado/

RUN pip install -r requirements.txt

COPY . /PIADockerizado/
