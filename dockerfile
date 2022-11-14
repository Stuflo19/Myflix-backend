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

WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]