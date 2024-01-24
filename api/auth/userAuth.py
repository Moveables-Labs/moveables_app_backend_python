from flask import Blueprint, request, jsonify
from flask_mail import BadHeaderError, Message

from api.extensions import emailManager
from dbmodel.ApiDatabaseModel import DatabaseManager
from models.ProviderModel import ProviderModel
from models.UserModel import UserModel
from utils.Tools import Tools

AuthApi = Blueprint('AuthApi', __name__)


@AuthApi.route('/loginuser', methods=['PUT'])
def logInUser():
    try:
        result = DatabaseManager.logInUser(request.json)
        return result
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


@AuthApi.route('/logoutuser', methods=['PUT'])
def logOutUser():
    try:
        result = DatabaseManager.logOutUser(request.json)
        return result
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


@AuthApi.route('/loginprovider', methods=['PUT'])
def logInProvider():
    try:
        result = DatabaseManager.logInProvider(request.json)
        return result
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


@AuthApi.route('/logoutprovider', methods=['PUT'])
def logOutProvider():
    try:
        result = DatabaseManager.logOutProvider(request.json)
        return result
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


# SIGN UP AND CREATING ANY USER IN DATABASE
@AuthApi.route('/signupuser', methods=['POST'])
def signUpUser():
    data = request.get_json()
    print(f"{type(data)}")
    # data = request.get_json()
    if data.get("provider") is not None:
        provider_model = ProviderModel(**data, isAuth=True, providerId=Tools.generateUUID())
        result = DatabaseManager.addToProviderDatabase(provider_model)  # create user in database
        return result
    user_model = UserModel(**data, isAuth=True, userId=Tools.generateUUID())
    result = DatabaseManager.addToUserDatabase(user_model)  # create user in database
    return result


# SIGN UP AND CREATING ANY PROVIDER IN DATABASE
@AuthApi.route('/signupprovider', methods=['POST'])
def signUpProvider():
    provider_model = ProviderModel(providerId=Tools.generateUUID(), isAuth=True, **request.json)
    result = DatabaseManager.addToProviderDatabase(provider_model)  # create user in database
    return result


# SEND VERIFICATION CODE TO USERS TO VERIFY EMAIL
@AuthApi.route('/verify_email', methods=['put'])

def sendVerificationEmail():
    try:
        data = request.get_json()
        code = Tools.generateNumber()  # generate a 5 digit code for user to verify email
        mail = emailManager()  # init the email manager
        message = Message(
            "Message Header",
            sender="noreply@demo.com",
            recipients=[data.get("receiveremail")])
        message.body = f"Your verification code is : {code}"
        mail.send(message)
        return jsonify({"status": True, "message": "Email sent successfully",
                        "data": {"receiver_email": data.get("receiveremail"), "code": code}}), 200
    except BadHeaderError:
        return jsonify({"status": False, "message": "Invalid header in email", "data": {}})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})
