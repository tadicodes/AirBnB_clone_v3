#!/usr/bin/python3
'''
Createw Flask app; and register the blueprint app_views to Flask instance app.
'''

from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
