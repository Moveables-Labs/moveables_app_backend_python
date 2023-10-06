from flask import Flask
from firebase_admin import credentials, initialize_app
from utils.constants import Constants


_cred = credentials.Certificate("utils/key.json")
_default_app = initialize_app(_cred)


def create_app():
    from .crud.userApi import UserApi
    from .auth.userAuth import AuthApi
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Constants.SECRET_KEY
    app.register_blueprint(UserApi, url_prefix=Constants.API_ROOT_DIR)
    app.register_blueprint(AuthApi, url_prefix=Constants.AUTH_ROOT_DIR)
    print(_default_app.name)
    return app
