from flask import Blueprint, request, jsonify, current_app, make_response
from .mongodb import get_movie
from .sqldb import verify
from flask_cors import cross_origin
import sys

api_page = Blueprint('api', __name__)

@api_page.route('/', methods=['GET'])
@cross_origin()
def api_get_movies():
    response = get_movie()

    return jsonify(response)

@api_page.route('/verify', methods=['POST'])
@cross_origin()
def verification():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        if verify(username,password):
            return {"token": username}
        else:
            return {"token": "error"}

# @api_page.route('/testsql', methods=['GET'])
# def testsql():
#     if not verify('stu@stu.com', 'password'):
#         return jsonify(token="123")


