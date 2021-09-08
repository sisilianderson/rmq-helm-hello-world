FROM python:3.9.6-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app
COPY ./requirements.txt /opt/
RUN pip install --disable-pip-version-check --no-cache-dir -r /opt/requirements.txt
COPY ./src /opt/app

ENTRYPOINT ["python", "main.py"]
