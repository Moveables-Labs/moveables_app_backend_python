from flask import Flask
from firebase_admin import credentials, initialize_app
# from .extentions import api, database


cred = credentials.Certificate("api/key.json")
default_app = initialize_app(cred)


def create_app():
    from .userApi import userApi
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'VutUi4uOvAYGP3PIeXXx2lPgTfWwAcDJeYIm2nA3'
    app.register_blueprint(userApi, url_prefix='/user')
    print(default_app.name)
    return app
