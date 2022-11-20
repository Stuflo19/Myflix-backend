# demo/__init__.py
from flask import Flask 
from .api import api_page
from flask_cors import CORS

app = Flask(__name__)

app.config.from_pyfile('settings.py')

app.register_blueprint(api_page)

if __name__ == "__main__":
    CORS(app)
    app.run(host='0.0.0.0', debug=True)
