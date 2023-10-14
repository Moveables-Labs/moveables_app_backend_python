from flask import Flask
# from firebase_admin import credentials, initialize_app
from utils.constants import Constants


def create_app():
    from .crud.userApi import UserApi
    from .crud.providerApi import ProviderApi
    from .auth.userAuth import AuthApi
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Constants.SECRET_KEY
    app.register_blueprint(UserApi, url_prefix=Constants.USER_API_ROOT_DIR)
    app.register_blueprint(
        ProviderApi, url_prefix=Constants.PROVIDER_API_ROOT_DIR)
    app.register_blueprint(AuthApi, url_prefix=Constants.AUTH_API_ROOT_DIR)
    return app
