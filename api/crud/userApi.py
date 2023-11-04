from flask import Blueprint, request, jsonify

from dbmodel.ApiDatabaseModel import ApiDatabaseModel
from models.UserModel import UserModel
from ..extensions import UserRef

UserApi = Blueprint('UserApi', __name__)


# CREATE AND POST USER TO DATABASE
@UserApi.route('/movableuser/create', methods=['POST'])
def createUser():
    try:
        user_model = ApiDatabaseModel.addToDatabase(
            UserModel().toDict()
        )
        return jsonify({"status": True, "message": "Post request was successful", "data": user_model}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


# UPDATE USER TOT DATABASE
@UserApi.route('/movableuser/update/userid=<string:id>', methods=['PUT'])
def updateUser(id):
    try:
        UserRef.document(id).set(request.json, merge=True)
        return jsonify({"status": True, "message": "Put request was successful", "data": request.json}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


# GET ALL THE USERS TO DATABASE
@UserApi.route('/movableuser/all', methods=['GET'])
def getAllUsers():
    try:
        # all_user = [users.to_dict() for users in UserRef.stream()]
        all_user = ApiDatabaseModel.getAllFromDatabase()
        print("*******************")
        print(all_user)
        return jsonify({'status': True, 'message': 'Successfully retrieved all users', 'data': all_user}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}}), 401


# GET SPECIFIC USER BY ID FROM DATABASE
@UserApi.route('/movableuser/get/userid=<string:id>', methods=['GET'])
def getUserById(id):
    try:
        users = UserRef.where(u"id", "==", id).stream()
        for user in users:
            userM = UserModel(**user.to_dict())
            print(f"User is {userM}")
            return jsonify({"status": True, "message": "User was  found", "data": user.to_dict()}), 200
        return jsonify({"status": True, "message": "User was not found", "data": request.json}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# DELETE OR REMOVE SPECIFIC USER FROM DATABASE
@UserApi.route('/movableuser/delete/userid=<string:id>', methods=['DELETE'])
def deleteUser(id):
    try:
        UserRef.document(id).delete()
        return jsonify({"status": True, "message": "User Is Deleted successfully", "data": {}}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# GET SPECIFIC USER BY EMAIL FROM DATABASE
@UserApi.route('/movableuser/get/useremail=<string:email>', methods=['GET'])
def getUserByEmail(email):
    try:
        users = UserRef.where(u"email", "==", email).stream()
        for user in users:
            userM = UserModel(**user.to_dict(), password="")
            print(f"User is {userM}")
            return jsonify({"status": True, "message": "User was  found", "data": user.to_dict()}), 200
        return jsonify({"status": True, "message": "User was not found", "data": request.json}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})
