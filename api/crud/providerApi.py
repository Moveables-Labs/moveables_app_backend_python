from flask import Blueprint, request, jsonify

from dbmodel.ApiDatabaseModel import DatabaseManager
from models.ProviderModel import ProviderModel
from utils.Tools import Tools

ProviderApi = Blueprint('ProviderApi', __name__)


# CREATE AND POST  PROVIDER TO DATABASE
@ProviderApi.route('/providermovableuser/create', methods=['POST'])
def createProvider():
    try:
        provider_model = DatabaseManager.addToProviderDatabase(
            ProviderModel(**request.json, providerId=Tools.generateUUID())
        )
        # providerRef = ProviderRef.document()
        # providerModel = ProviderModel(
        #     id=ProviderRef.id, dateTime=Tools.getCurrentTime(), **request.json)
        # providerRef.set(providerModel.toDict())
        return jsonify({"status": True, "message": "Post request was successful", "data": provider_model}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


# UPDATE PROVIDER TO DATABASE
@ProviderApi.route('/providermovableuser/update/providerid=<string:providerId>', methods=['PUT'])
def updateProvider(providerId):
    try:
        DatabaseManager.updateProviderDatabase(providerId, request.json)
        return jsonify({"status": True, "message": "Put request was successful", "data": request.json}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


# GET ALL THE PROVIDERS TO DATABASE
@ProviderApi.route('/providermovableuser/all', methods=['GET'])
def getAllProviders():
    try:
        all_provider = DatabaseManager.getAllFromProviderDatabase()
        return jsonify(
            {'status': True, 'message': 'Successfully retrieved all provider users', 'data': all_provider}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# GET SPECIFIC PROVIDER BY ID FROM DATABASE
@ProviderApi.route('/providermovableuser/get/providerid=<string:providerId>', methods=['GET'])
def getProviderById(providerId):
    try:
        # for provider in ProviderRef.stream():
        #     providerModel = ProviderModel(**provider.to_dict())
        #     if (providerModel.id == id):
        # return jsonify(), 200
        provider = DatabaseManager.getByIdFromProviderDatabase(providerId)
        return jsonify({"status": True, "message": "Provider was found", "data": provider})
        # return jsonify({"status": True, "message": "Provider was not found", "data": request.json})
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


@ProviderApi.route('/providermovableuser/get/email=<string:email>', methods=['GET'])
def getProviderByEmail(email):
    try:
        # for provider in ProviderRef.stream():
        #     providerModel = ProviderModel(**provider.to_dict())
        #     if (providerModel.id == id):
        # return jsonify(), 200
        provider = DatabaseManager.getByEmailFromProviderDatabase(email)
        return jsonify({"status": True, "message": "Provider was found", "data": provider})
        # return jsonify({"status": True, "message": "Provider was not found", "data": request.json})
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# DELETE OR REMOVE SPECIFIC PROVIDER FROM DATABASE
@ProviderApi.route('/providermovableuser/delete/providerid=<string:providerId>', methods=['DELETE'])
def deleteProvider(providerId):
    try:
        # ProviderRef.document(id).delete()
        result = DatabaseManager.deleteFromProviderDatabase(providerId)
        pos_message = "Provider Is Deleted successfully"
        neg_message = "Deleting Provider was not successful"
        return jsonify(
            {"status": True, "message": pos_message if result["successCode"] else neg_message, "data": {}}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})
