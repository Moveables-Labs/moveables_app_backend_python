from firebase_admin import firestore
from utils.constants import Constants
from firebase_admin import credentials, initialize_app, auth


Cred = credentials.Certificate("utils/key.json")
Initialize = initialize_app(Cred)
DataBase = firestore.client()
UserRef = DataBase.collection(Constants.USERS_DB_COLLECTION_NAME)
ProviderRef = DataBase.collection(Constants.PROVIDER_DB_COLLECTION_NAME)
