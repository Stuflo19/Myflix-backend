from flask import Blueprint, request, jsonify, current_app, make_response
from .mongodb import get_movie, get_genres
from .sqldb import verify
from .stream import initiate_stream
from flask_cors import cross_origin
import sys

api_page = Blueprint('api', __name__)

@api_page.route('/movies', methods=['GET', 'POST'])
@cross_origin()
def api_get_movies():
    response = get_movie(request.json)

    return jsonify(response)

@api_page.route('/genres', methods=['GET'])
@cross_origin()
def api_get_genres():
    response = get_genres()

    return jsonify(response)

@api_page.route('/verify', methods=['GET', 'POST'])
@cross_origin()
def verification():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        if verify(username,password):
            return {"token": username}, 200
        else:
            return {"token": "error"}, 200

@api_page.route('/stream', methods=['GET', 'POST'])
@cross_origin()
def start_stream():
    filename = request.json['filename']
    response = initiate_stream(filename)
    if response == "success":
        return '', 200
    if response == "error":
        return '', 404


@api_page.route('/health')
def health():
    return '', 200

@api_page.route('/ready')
def ready():
    return '', 200

# @api_page.route('/testsql', methods=['GET'])
# def testsql():
#     if not verify('stu@stu.com', 'password'):
#         return jsonify(token="123")
