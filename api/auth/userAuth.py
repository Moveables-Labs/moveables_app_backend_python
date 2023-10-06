from flask import Blueprint


AuthApi = Blueprint('AuthApi', __name__)


@AuthApi.route('/')
def home():
    return "Hello World"
