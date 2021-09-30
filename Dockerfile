FROM python:3.9.7-slim-buster

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser &&\
    chown -R appuser /app
USER appuser

COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app"

ENV FLASK_ENV=development
CMD python -m siren
