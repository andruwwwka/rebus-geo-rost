FROM python:3.8.2-alpine3.11

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -U pip

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:80 rebus_hackaton.wsgi:application"]
