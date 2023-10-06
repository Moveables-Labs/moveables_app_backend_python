import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from utils.constants import Constants
from api.UserModel import UserModel
from utils.Tools import Tools

db = firestore.client()
user_Ref = db.collection(Constants.DB_COLLECTION_NAME)
userApi = Blueprint('userApi', __name__)


@userApi.route('/movableuser/create', methods=['POST'])
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


@userApi.route('/movableuser/update/userid=<string:id>', methods=['PUT'])
def updateUser(id):
    try:
        user_Ref.document(id).set(request.json, merge=True)
        return jsonify({"status": True, "message": "Put request was successful", "data": request.json}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


@userApi.route('/movableuser/all', methods=['GET'])
def getAllUsers():
    try:
        all_user = [users.to_dict() for users in user_Ref.stream()]
        return jsonify({'status': True, 'message': 'Get all user successful', 'data': all_user}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


@userApi.route('/movableuser/get/userid=<string:id>', methods=['GET'])
def getUser(id):
    try:
        for user in user_Ref.stream():
            userM = UserModel(**user.to_dict())
            if (userM.id == id):
                print(userM)
                return jsonify(user.to_dict()), 200
        return jsonify({"status": True, "message": "User was not found", "data": request.json}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


@userApi.route('/movableuser/delete/userid=<string:id>', methods=['DELETE'])
def deleteUser(id):
    try:
        user_Ref.document(id).delete()
        return jsonify({"status": True, "message": "User Is Deleted successfully", "data": {}}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})
