from firebase_admin import firestore
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from utils.constants import Constants
from firebase_admin import credentials, initialize_app, auth

Cred = credentials.Certificate("utils/key.json")
Initialize = initialize_app(Cred)
DataBase = firestore.client()
UserRef = DataBase.collection(Constants.USERS_DB_COLLECTION_NAME)
ProviderRef = DataBase.collection(Constants.PROVIDER_DB_COLLECTION_NAME)
Auth = auth


def createApp():
    from api import App
    from .crud.userApi import UserApi
    from .crud.providerApi import ProviderApi
    from .auth.userAuth import AuthApi
    App.register_blueprint(UserApi, url_prefix=Constants.USER_API_ROOT_DIR)
    App.register_blueprint(
        ProviderApi, url_prefix=Constants.PROVIDER_API_ROOT_DIR)
    App.register_blueprint(AuthApi, url_prefix=Constants.AUTH_API_ROOT_DIR)
    return App


def initDatabase():
    from api import App
    # initialize db
    # init the database
    App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apidatabase.db'
    return SQLAlchemy(App)


def emailManager():
    from api import App
    # init the app so it can send emails
    App.config['MAIL_SERVER'] = 'smtp.gmail.com'
    App.config['MAIL_PORT'] = 465
    App.config['MAIL_USERNAME'] = "aigbojeohiorenua@gmail.com"  # sender email
    App.config['MAIL_PASSWORD'] = "nldz nicr pyvx htgl"  # sender password
    App.config['MAIL_USE_TLS'] = False
    App.config['MAIL_USE_SSL'] = True
    return Mail(App)
