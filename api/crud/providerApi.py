from flask import Blueprint, request, jsonify
from models.UserModel import UserModel
from utils.Tools import Tools
from ..extensions import ProviderRef

ProviderApi = Blueprint('ProviderApi', __name__)


# CREATE AND POST USER TO DATABASE


@ProviderApi.route('/providermovableuser/create', methods=['POST'])
def createUser():
    try:
        user_ref = ProviderRef.document()
        userModel = UserModel(
            id=user_ref.id, dateTime=Tools.getCurrentTime(), **request.json)
        user_ref.set(userModel.toDict())
        return jsonify({"status": True, "message": "Post request was successful", "data": userModel}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


# CREATE OR UPDATE USER TOT DATABASE
@ProviderApi.route('/providermovableuser/update/userid=<string:id>', methods=['PUT'])
def updateUser(id):
    try:
        ProviderRef.document(id).set(request.json, merge=True)
        return jsonify({"status": True, "message": "Put request was successful", "data": request.json}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


# GET ALL THE USERS TO DATABASE
@ProviderApi.route('/providermovableuser/all', methods=['GET'])
def getAllUsers():
    try:
        all_user = [users.to_dict() for users in ProviderRef.stream()]
        return jsonify({'status': True, 'message': 'Successfully retrieved all provider users', 'data': all_user}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# GET SPECIFICC USER BY ID FROM DATABASE
@ProviderApi.route('/providermovableuser/get/userid=<string:id>', methods=['GET'])
def getUser(id):
    try:
        for user in ProviderRef.stream():
            userM = UserModel(**user.to_dict())
            if (userM.id == id):
                print(userM)
                return jsonify(user.to_dict()), 200
        return jsonify({"status": True, "message": "User was not found", "data": request.json}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# DELETE OR REMOVE SPECIFIC USER FROM DATABASE
@ProviderApi.route('/providermovableuser/delete/userid=<string:id>', methods=['DELETE'])
def deleteUser(id):
    try:
        ProviderRef.document(id).delete()
        return jsonify({"status": True, "message": "User Is Deleted successfully", "data": {}}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})
