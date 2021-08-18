FROM python:3.9.6

RUN pip install poetry
RUN poetry install

WORKDIR /app/

COPY . .
