FROM python:3.7.15-alpine3.17

RUN apk add build-base
RUN apk add --no-cache openssl-dev libffi-dev

RUN pip3 install pipenv

ENV FLASK_APP MyFlix_API.app
ENV FLASK_DEBUG 1

ENV MONGO_URI mongodb://root:password123@mongo/myflix?authSource=admin

ENV MYSQL_HOST sql
ENV MYSQL_USER root
ENV MYSQL_PASSWORD password123
ENV MYSQL_DB netflix

WORKDIR /app

COPY . /app
RUN pipenv install --system --ignore-pipfile

# Development
CMD ["flask", "run", "--host", "0.0.0.0"]