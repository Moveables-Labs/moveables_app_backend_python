from flask import Blueprint, request, jsonify
from flask_mail import BadHeaderError, Message

from api.extensions import emailManager
from dbmodel.ApiDatabaseModel import DatabaseManager
from models.ProviderModel import ProviderModel
from models.UserModel import UserModel
from utils.Tools import Tools

AuthApi = Blueprint('AuthApi', __name__)


@AuthApi.route('/login/email=<string:email>/password=<string:password>')
def logIn(email, password):
    return f"Your Email : {email} Password : {password}, message : Not Implemented"


# SIGN UP AND CREATING ANY USER IN DATABASE
@AuthApi.route('/signupuser', methods=['POST'])
def signUpUser():
    try:
        user_model = UserModel(**request.json, isAuth=True, userId=Tools.generateUUID())
        result = DatabaseManager.addToUserDatabase(user_model)  # create user in database
        # UserModel(**request.json)
        # Auth.create_user(uid=user_model.id, email=user_model.email,
        #                  password=user_model.password)  # create user in authentication
        # UserRef.document(user_model.id).set(user_model.toDict())  # create user in firestore database
        return jsonify(
            {"status": True, "message": f"User with email {user_model.email} created", "data": result})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}",
                        "data": {}})  # SIGN UP AND CREATING ANY USER IN DATABASE


# SIGN UP AND CREATING ANY PROVIDER IN DATABASE
@AuthApi.route('/signupprovider', methods=['POST'])
def signUpProvider():
    try:
        provider_model = ProviderModel(providerId=Tools.generateUUID(), isAuth=True, **request.json)
        # Auth.create_user(uid=provider_model.id, email=provider_model.email,
        #                  password=provider_model.password)  # create user in authentication
        # ProviderRef.document(provider_model.id).set(provider_model.toDict())  # create user in firestore database
        return jsonify({"status": True, "message": f"User with email {provider_model.email} created",
                        "data": provider_model.toDict()})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


# # SIGN UP WITHOUT CREATING ANY USER IN DATABASE
# @AuthApi.route('/signup', methods=['POST'])
# def signUp():
#     try:
#         user_model = UserModel(id=Tools.generateUUID(), **request.json)
#         Auth.create_user(uid=user_model.id, email=user_model.email,
#                          password=user_model.password)  # create user in authentication
#         return jsonify(
#             {"status": True, "message": f"User with email {user_model.email} created", "data": user_model.toDict()})
#     except Exception as e:
#         return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


# SEND VERIFICATION CODE TO USERS TO VERIFY EMAIL
@AuthApi.route('/verify_email/receiver_email=<string:receiver_email>', methods=['GET'])
def sendVerificationEmail(receiver_email):
    try:
        code = Tools.generateNumber()  # generate a 5 digit code for user to verify email
        mail = emailManager()  # init the email manager
        message = Message("Message Header", sender="noreply@demo.com", recipients=[receiver_email])
        message.body = f"Your verification code is : {code}"
        mail.send(message)
        return jsonify({"status": True, "message": "Email sent successfully",
                        "data": {"receiver_email": receiver_email, "code": code}}), 200
    except BadHeaderError:
        return jsonify({"status": False, "message": "Invalid header in email", "data": {}})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})
