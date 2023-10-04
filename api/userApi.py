import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('user')
userApi = Blueprint('userApi', __name__)


@userApi.route('/post', methods=['POST'])
def post():
    try:
        id = uuid.uuid4()
        user_Ref.document(id.hex).set(request.json)
        return jsonify({"Succsess": True}), 200
    except Exception as e:
        return f"An Error Has Occured: {e}"


@userApi.route('/getall', methods=['GET'])
def getAll():
    try:
        all_user = [users.to_dict() for users in user_Ref.stream()]
        return jsonify(all_user), 200
    except Exception as e:
        return f'An Error of : {e}'
