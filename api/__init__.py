import os
from flask import Flask
from utils.constants import Constants

App: Flask
basedir = os.path.abspath(os.path.dirname(__file__))

App = Flask(__name__)
App.config['SECRET_KEY'] = Constants.SECRET_KEY
