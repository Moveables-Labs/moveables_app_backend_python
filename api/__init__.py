import os
from flask import Flask
from utils.constants import Constants
from flask_mail import Mail

_App = Flask
basedir = os.path.abspath(os.path.dirname(__file__))


def createApp():
    global _App
    from .crud.userApi import UserApi
    from .crud.providerApi import ProviderApi
    from .auth.userAuth import AuthApi
    _App = Flask(__name__)
    _App.config['SECRET_KEY'] = Constants.SECRET_KEY
    _App.register_blueprint(UserApi, url_prefix=Constants.USER_API_ROOT_DIR)
    _App.register_blueprint(
        ProviderApi, url_prefix=Constants.PROVIDER_API_ROOT_DIR)
    _App.register_blueprint(AuthApi, url_prefix=Constants.AUTH_API_ROOT_DIR)
    return _App


def emailManager():
    # init the app so it can send emails
    _App.config['MAIL_SERVER']='smtp.gmail.com'
    _App.config['MAIL_PORT'] = 465
    _App.config['MAIL_USERNAME'] = "aigbojeohiorenua@gmail.com" # sender email
    _App.config['MAIL_PASSWORD'] = "nldz nicr pyvx htgl" # sender password
    _App.config['MAIL_USE_TLS'] = False
    _App.config['MAIL_USE_SSL'] = True
    return Mail(_App)
