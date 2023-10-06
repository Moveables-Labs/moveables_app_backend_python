from firebase_admin import firestore
from flask import Blueprint
from utils.constants import Constants

DataBase = firestore.client()
UserRef = DataBase.collection(Constants.DB_COLLECTION_NAME)
