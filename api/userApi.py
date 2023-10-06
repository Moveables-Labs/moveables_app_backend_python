import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from utils.constants import Constants
from api.UserModel import UserModel
from utils.Tools import Tools

db = firestore.client()
user_Ref = db.collection(Constants.DB_COLLECTION_NAME)
userApi = Blueprint('userApi', __name__)


@userApi.route('/create', methods=['POST'])
def createUser():
    try:
        user_ref = db.collection(
            Constants.DB_COLLECTION_NAME).document()
        userModel = UserModel(
            id=user_ref.id, dateTime=Tools.getCurrentTime(), **request.json)
        user_ref.set(userModel.toDict())
        return jsonify({"status": True, "message": "Post request was successful", "data": userModel}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


@userApi.route('/update', methods=['PUT'])
def updateUser():
    try:
        id = request.json["id"]
        user_Ref.document(id).set(request.json, merge=True)
        return jsonify({"status": True, "message": "Post request was successful", "data": request.json}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


@userApi.route('/all', methods=['GET'])
def getAllUsers():
    try:
        all_user = [users.to_dict() for users in user_Ref.stream()]
        return jsonify(all_user), 200
    except Exception as e:
        return f'An Error of : {e}'


@userApi.route('/one', methods=['GET'])
def getUser():
    try:
        for user in user_Ref.stream():
            print(UserModel(**user.to_dict()))
            return jsonify(user.to_dict()), 200
    except Exception as e:
        return f'An Error of : {e}'
