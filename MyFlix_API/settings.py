#demo/settings.py
from os import environ 

MONGO_URI = environ.get('MONGO_URI')

MYSQL_DATABASE_HOST = environ.get('MYSQL_HOST')
MYSQL_DATABASE_DB = environ.get('MYSQL_DB')
MYSQL_DATABASE_USER = environ.get('MYSQL_USER')
MYSQL_DATABASE_PASSWORD = environ.get('MYSQL_PASSWORD')
