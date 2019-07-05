FROM python:3.6.8-alpine

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -U pip

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:80 rebus_hackaton.wsgi:application"]
