from flask import Blueprint, request, jsonify
from models.ProviderModel import ProviderModel
from utils.Tools import Tools
from ..extensions import ProviderRef

ProviderApi = Blueprint('ProviderApi', __name__)


# CREATE AND POST  PROVIDER TO DATABASE
@ProviderApi.route('/providermovableuser/create', methods=['POST'])
def createProvider():
    try:
        providerRef = ProviderRef.document()
        providerModel = ProviderModel(
            id=ProviderRef.id, dateTime=Tools.getCurrentTime(), **request.json)
        providerRef.set(providerModel.toDict())
        return jsonify({"status": True, "message": "Post request was successful", "data": providerModel}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


# CREATE OR UPDATE PROVIDER TO DATABASE
@ProviderApi.route('/providermovableuser/update/providerid=<string:id>', methods=['PUT'])
def updateProvider(id):
    try:
        ProviderRef.document(id).set(request.json, merge=True)
        return jsonify({"status": True, "message": "Put request was successful", "data": request.json}), 200
    except Exception as e:
        return jsonify({"status": False, "message": f"An Error Has Occured: {e}", "data": {}})


# GET ALL THE PROVIDERS TO DATABASE
@ProviderApi.route('/providermovableuser/all', methods=['GET'])
def getAllProviders():
    try:
        allProvider = [provider.to_dict() for provider in ProviderRef.stream()]
        return jsonify({'status': True, 'message': 'Successfully retrieved all provider users', 'data': allProvider}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# GET SPECIFICC PROVIDER BY ID FROM DATABASE
@ProviderApi.route('/providermovableuser/get/providerid=<string:id>', methods=['GET'])
def getProvider(id):
    try:
        for provider in ProviderRef.stream():
            providerModel = ProviderModel(**provider.to_dict())
            if (providerModel.id == id):
                return jsonify({"status": True, "message": "Provider was found", "data": providerModel.toDict()})
                #return jsonify(), 200
        return jsonify({"status": True, "message": "Provider was not found", "data": request.json})
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})


# DELETE OR REMOVE SPECIFIC PROVIDER FROM DATABASE
@ProviderApi.route('/providermovableuser/delete/providerid=<string:id>', methods=['DELETE'])
def deleteProvider(id):
    try:
        ProviderRef.document(id).delete()
        return jsonify({"status": True, "message": "Provider Is Deleted successfully", "data": {}}), 200
    except Exception as e:
        return jsonify({'status': False, 'message': f'An Error of : {e}', 'data': {}})
