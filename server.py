from flask import Flask
from flask_cors import CORS, cross_origin
from core.routing import load_routes


'''
    Application entry point
    Initialize Cross Origin Ressource Sharing for remote access
    Initialize routing from core/routing.py

'''
app = Flask(__name__)
CORS(app)
load_routes(app)
