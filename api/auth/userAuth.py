import email
from flask import Blueprint, request, jsonify
from api.extensions import ProviderRef, auth

from models.CreateUserModel import CreateUserModel
from models.UserModel import UserModel
from utils.Tools import Tools

AuthApi = Blueprint('AuthApi', __name__)




@AuthApi.route('/login/email=<string:email>/password=<string:password>')
def logIn(email, password):
    return f"Your Email : {email} Passwprd : {password}"


# SIGN UP AND CREATING ANY USER IN DATABASE
@AuthApi.route('/signupwithdata', methods=['POST'])
def signUpWithData():
    try:
        user_model = UserModel(id=Tools.generateUUID(), **request.json)
        auth.create_user(uid = user_model.id, email=user_model.email, password=user_model.password)
        ProviderRef.document(user_model.id).set(user_model.toDict())
        return jsonify({"status": True, "message": f"User with email {user_model.email} created", "data": user_model.toDict()})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})

# SIGN UP WITH OUT CREATING ANY USER IN DATABASE
@AuthApi.route('/signup', methods=['POST'])
def signUp():
    try:
        user_model = UserModel(id=Tools.generateUUID(), **request.json)
        auth.create_user(uid = user_model.id, email=user_model.email, password=user_model.password)
        return jsonify({"status": True, "message": f"User with email {user_model.email} created", "data": user_model.toDict()})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})
