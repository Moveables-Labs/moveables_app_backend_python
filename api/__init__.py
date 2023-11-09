from flask import Flask
from flask_socketio import SocketIO
from utils.constants import Constants
from flask_mail import Mail

_App = Flask

def createApp():
    global _App
    from .crud.userApi import UserApi
    from .crud.providerApi import ProviderApi
    from .auth.userAuth import AuthApi
    _App = Flask(__name__, template_folder="../templates")
        # add database
    _App.config['SECRET_KEY'] = Constants.SECRET_KEY
    #_App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
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

def getSocket():
    socketIO = SocketIO(_App, cors_allowed_origins='*')
    return socketIO

