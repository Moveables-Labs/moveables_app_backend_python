from flask import Blueprint, request, jsonify
from api.extensions import ProviderRef, auth
from models.UserModel import UserModel
from utils.Tools import Tools
from api import emailManager
from flask_mail import BadHeaderError, Message

AuthApi = Blueprint('AuthApi', __name__)




@AuthApi.route('/login/email=<string:email>/password=<string:password>')
def logIn(email, password):
    return f"Your Email : {email} Passwprd : {password}, message : Not Implemented"


# SIGN UP AND CREATING ANY USER IN DATABASE
@AuthApi.route('/signupwithdata', methods=['POST'])
def signUpWithData():
    try:
        user_model = UserModel(id=Tools.generateUUID(), **request.json)
        auth.create_user(uid = user_model.id, email=user_model.email, password=user_model.password) # create user in authentication
        ProviderRef.document(user_model.id).set(user_model.toDict()) # create user in firestor database
        return jsonify({"status": True, "message": f"User with email {user_model.email} created", "data": user_model.toDict()})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})

# SIGN UP WITH OUT CREATING ANY USER IN DATABASE
@AuthApi.route('/signup', methods=['POST'])
def signUp():
    try:
        user_model = UserModel(id=Tools.generateUUID(), **request.json)
        auth.create_user(uid = user_model.id, email=user_model.email, password=user_model.password) # create user in authentication
        return jsonify({"status": True, "message": f"User with email {user_model.email} created", "data": user_model.toDict()})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


# SEND VERIFICATION CODE TO USERS TO VERIFY EMAIL
@AuthApi.route('/verifyemail/recivermail=<string:reciveremail>', methods=['GET'])
def sendVerificationEmail(reciveremail):
    try:    
        code = Tools.generateNumber() # generate a 5 digit code for user to verify email
        mail = emailManager() # init the email manager
        message = Message("Message Header", sender="noreply@demo.com", recipients= [reciveremail])
        message.body = f"Your verification code is : {code}" 
        mail.send(message)
        return jsonify({"status": True, "message": "Email sent successfully", "data": {"reciveremail" : reciveremail, "code" : code}}), 200
    except BadHeaderError:
        return jsonify({"status": False, "message": "Invalid header in email", "data": {}})
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})