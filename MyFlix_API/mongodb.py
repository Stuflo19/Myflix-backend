import bson

from bson.json_util import dumps
from flask import current_app, g, json, request
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

def get_mongodb():
    if 'mongodb' not in g:
        g.mongodb = PyMongo(current_app).db

    return g.mongodb

# Use LocalProxy to read the global db instance with just `db`
mongodb = LocalProxy(get_mongodb)

def get_movie(genre):
    movie = list(mongodb.movies.find(genre))
    return json_response(movie)

def get_genres():
    genres = list(mongodb.genres.find())
    return json_response(genres)

def json_response(payload, status=200):
  return (dumps(payload), status, {'content-type': 'application/json'})
