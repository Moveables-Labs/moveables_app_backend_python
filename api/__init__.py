from flask import Flask
from firebase_admin import credentials, initialize_app
from utils.constants import Constants


cred = credentials.Certificate("api/key.json")
default_app = initialize_app(cred)


def create_app():
    from .userApi import userApi
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Constants.SECRET_KEY
    app.register_blueprint(userApi, url_prefix=Constants.API_ROOT_DIR)
    print(default_app.name)
    return app
