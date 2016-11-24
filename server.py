from flask import Flask
from flask_cors import CORS, cross_origin
from core.routing import init_route

app = Flask(__name__)
CORS(app)
init_route(app)
