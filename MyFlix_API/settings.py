#demo/settings.py
import os

MONGO_URI = os.getenv('MONGO_URI')

MYSQL_DATABASE_HOST = os.getenv('MYSQL_HOST')
MYSQL_DATABASE_DB = os.getenv('MYSQL_DB')
MYSQL_DATABASE_USER = os.getenv('MYSQL_USER')
MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD')
