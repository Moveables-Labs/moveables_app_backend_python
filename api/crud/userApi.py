from flask import Blueprint, request, jsonify

from dbmodel.ApiDatabaseModel import DatabaseManager
from models.UserModel import UserModel
from utils.Tools import Tools

UserApi = Blueprint('UserApi', __name__)


# CREATE AND POST USER TO DATABASE
@UserApi.route('/movablesuser/create', methods=['POST'])
def createUser():
    try:
        user_model = DatabaseManager.addToUserDatabase(
            UserModel(**request.json, userId=Tools.generateUUID())
        )
        return jsonify({"status": True, "message": "Post request was successful", "data": user_model}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


# UPDATE USER TOT DATABASE
@UserApi.route('/movablesuser/update/userid=<string:userId>', methods=['PUT'])
def updateUser(userId):
    try:
        DatabaseManager.updateUserDatabase(userId, request.json)
        return jsonify({"status": True, "message": "Put request was successful", "data": request.json}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occurred: {e}", "data": {}})


# GET ALL THE USERS TO DATABASE
@UserApi.route('/movablesuser/all', methods=['GET'])
def getAllUsers():
    try:
        # all_user = [users.to_dict() for users in UserRef.stream()]
        all_user = DatabaseManager.getAllFromUserDatabase()
        return jsonify({'status': True, 'message': 'Successfully retrieved all users', 'data': all_user}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}}), 401


# GET SPECIFIC USER BY ID FROM DATABASE
@UserApi.route('/movablesuser/get/userid=<string:userId>', methods=['GET'])
def getUserById(userId):
    try:
        user = DatabaseManager.getByIdFromUserDatabase(userId)
        # users = UserRef.where(u"id", "==", id).stream()
        # for user in users:
        #     userM = UserModel(**user.to_dict())
        #     print(f"User is {userM}")
        #     return jsonify({"status": True, "message": "User was  found", "data": user.to_dict()}), 200
        return jsonify({"status": True, "message": "User was  found", "data": user}), 200
        # return jsonify({"status": True, "message": "User was not found", "data": request.json}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# DELETE OR REMOVE SPECIFIC USER FROM DATABASE
@UserApi.route('/movablesuser/delete/userid=<string:userId>', methods=['DELETE'])
def deleteUser(userId):
    try:
        result = DatabaseManager.deleteFromUserDatabase(userId)
        pos_message = "User Is Deleted successfully"
        neg_message = "Deleting user was not successful"
        # UserRef.document(id).delete()
        return jsonify(
            {"status": True, "message": pos_message if result["successCode"] else neg_message, "data": result}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# GET SPECIFIC USER BY EMAIL FROM DATABASE
@UserApi.route('/movablesuser/get/useremail=<string:email>', methods=['GET'])
def getUserByEmail(email):
    try:
        user = DatabaseManager.getByEmailFromUserDatabase(email)
        return jsonify({"status": True, "message": "User was  found", "data": user}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})
