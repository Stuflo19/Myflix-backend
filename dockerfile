FROM ubuntu

RUN apt update
RUN apt install python3-pip -y

RUN pip3 install FLASK
RUN pip3 install Flask-PyMongo
RUN pip3 install Flask-CORS
RUN pip3 install python-dotenv
RUN pip3 install Flask-socketio
RUN pip3 install devpi
RUN pip3 install Flask_mysql
RUN pip3 install cryptography
RUN pip3 install gunicorn

ENV FLASK_APP MyFlix_API.app
ENV FLASK_DEBUG 1

ENV MONGO_URI mongodb://root:password123@mongo/myflix?authSource=admin

ENV MYSQL_HOST sql
ENV MYSQL_USER root
ENV MYSQL_PASSWORD password123
ENV MYSQL_DB netflix

WORKDIR /app

COPY . /app

# Development
CMD ["flask", "run", "--host", "0.0.0.0"]