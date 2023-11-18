# import json
# from dataclasses import dataclass, asdict
# from datetime import datetime
#
# from api.extensions import initDatabase
# from models.OrderDelivery import DeliveryModel
#
# _database = initDatabase()
#
#
# class ApiDatabaseModel(_database.Model):
#     id = _database.Column(_database.Integer, primary_key=True)
#     userId = _database.Column(_database.Integer, nullable=False)
#     password = _database.Column(_database.String(100), nullable=False)
#     email = _database.Column(_database.String(100), nullable=False)
#     firstName = _database.Column(_database.String(100), nullable=True)
#     lastName = _database.Column(_database.String(100), nullable=True)
#     phoneNumber = _database.Column(_database.String(100), nullable=True)
#     state = _database.Column(_database.String(100), nullable=True)
#     dateTime = _database.Column(_database.DateTime, default=datetime.utcnow())
#     address = _database.Column(_database.String(100), nullable=True)
#
#     def __repr__(self):
#         return f"<Name> {self.email}"
#
#     @staticmethod
#     def addToDatabase(api_database_model):
#         try:
#             _database.session.add(api_database_model)
#             _database.session.commit()
#             return "Success", 1
#         except Exception as e:
#             return f"{e}", 0
#
#     @staticmethod
#     def getAllFromDatabase():
#         results: list = []
#         try:
#             result = _database.session.query(ApiDatabaseModel).all()
#             for r in result:
#                 # Remove the item with key "b"
#                 if "_sa_instance_state" in r.__dict__:
#                     del r.__dict__["_sa_instance_state"]
#                     results.append(r.__dict__)
#                 else:
#                     results.append(r.__dict__)
#             return results
#         except Exception as e:
#             return [{'error': f"{e}"}]
import json

from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Boolean, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models.ProviderModel import ProviderModel
from models.UserModel import UserModel

_Base = declarative_base()


class MovableUser(_Base):
    __tablename__ = "MovableUsers"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    isAuth = Column(Boolean)
    isLogIn = Column(Boolean)
    password = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    phoneNumber = Column(String)
    state = Column(String)
    userId = Column(String)
    address = Column(String)
    defaultLocation = Column(String)
    fareCost = Column(String)
    paymentInfo = Column(String)
    communicationData = Column(String)
    order = Column(String)
    deliveryModel = Column(String)
    dateTime = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, user_model: UserModel):
        self.email = user_model.email
        self.isAuth = user_model.isAuth
        self.isLogIn = user_model.isLogIn
        self.password = user_model.password
        self.firstName = user_model.firstName
        self.lastName = user_model.lastName
        self.phoneNumber = user_model.phoneNumber
        self.state = user_model.state
        self.userId = user_model.userId
        self.address = user_model.address
        self.defaultLocation = json.dumps(user_model.defaultLocation.toDict())
        self.fareCost = json.dumps(user_model.fareCost.toDict())
        self.paymentInfo = json.dumps(user_model.paymentInfo.toDict())
        self.communicationData = json.dumps(user_model.communicationData.toDict())
        self.order = json.dumps(user_model.order.toDict())
        self.deliveryModel = json.dumps(user_model.deliveryModel.toDict())

    def __repr__(self):
        return f"MovableUser(id={self.id}, email={self.email}, password={self.password}, "


class MovableProvider(_Base):
    __tablename__ = "MovableProvider"
    id = Column(Integer, primary_key=True)
    state = Column(String)
    email = Column(String)
    isAuth = Column(Boolean)
    isLogIn = Column(Boolean)
    dateTime = Column(DateTime(timezone=True), server_default=func.now())
    password = Column(String)
    providerId = Column(String)
    companyName = Column(String)
    phoneNumber = Column(String)
    deliveryModel = Column(String)
    deliveryMethod = Column(String)
    companyAddress = Column(String)
    defaultLocation = Column(String)
    communicationData = Column(String)

    def __init__(self, provider_model: ProviderModel):
        self.state = provider_model.state
        self.email = provider_model.email
        self.isAuth = provider_model.isAuth
        self.isLogIn = provider_model.isLogIn
        self.password = provider_model.password
        self.providerId = provider_model.providerId
        self.companyName = provider_model.companyName
        self.phoneNumber = provider_model.phoneNumber
        self.deliveryModel = json.dumps(
            provider_model.deliveryModel.toDict())  # provider_model.deliveryModel.toDict().__str__()
        self.deliveryMethod = provider_model.deliveryMethod.__str__()
        self.companyAddress = provider_model.companyAddress
        self.defaultLocation = json.dumps(provider_model.defaultLocation.toDict())
        self.communicationData = json.dumps(provider_model.communicationData.toDict())

    def __repr__(self):
        return f"MovableProvider(id={self.id}, email={self.email}, password={self.password}, "


_engine = create_engine('sqlite:///dbmodel/apidatabase.db', echo=True)
_Base.metadata.create_all(bind=_engine)
_Session = sessionmaker(bind=_engine)
_session = _Session()


class DatabaseManager:
    # ******* MovableUser method call for interacting with database ***********
    @staticmethod
    def addToUserDatabase(user_model: UserModel):
        try:
            _session.add(MovableUser(user_model))
            _session.commit()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def updateUserDatabase(userId: str, values: dict):
        try:
            _session.query(MovableUser).filter_by(userId=userId).update(values)  # .add(MovableUser(user_model))
            _session.commit()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def logInUser(result):
        print(F"RESULT : {result}")
        user = DatabaseManager.getByEmailFromUserDatabase(result["email"])
        if user["password"] == result["password"]:
            DatabaseManager.updateUserDatabase(user["userId"], {"email": "mail@me.com"})
            return "Success"
        raise Exception(f"User with email {result['email']} and password {result['password']} was not found")

    @staticmethod
    def logOutUser(result):
        print(F"RESULT : {result}")
        user = DatabaseManager.getByEmailFromUserDatabase(result["email"])
        if user["password"] == result["password"]:
            DatabaseManager.updateUserDatabase(user["userId"], {"isLogIn": False})
            return "Success"
        raise Exception(f"User with email {result['email']} and password {result['email']} was not found")

    @staticmethod
    def deleteFromUserDatabase(user_model: str):
        try:
            _session.query(MovableUser).filter_by(userId=user_model).delete()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def getAllFromUserDatabase():
        results: list = []
        try:
            for value in _session.query(MovableUser).all():
                result = value
                for k, v in result.__dict__.items():
                    try:
                        result.__dict__[k] = json.loads(v)
                    except Exception as e:
                        print(f"ERR Key {k} Value {v}")
                        print(f"ERROR {e}")

                # Remove the item with key "b"
                if "_sa_instance_state" in result.__dict__:
                    del result.__dict__["_sa_instance_state"]
                    results.append(result.__dict__)
                else:
                    results.append(result.__dict__)
            return results
        except Exception as e:
            return [{'error': f"{e}"}]

    @staticmethod
    def getByIdFromUserDatabase(userId: str):
        try:
            value = _session.query(MovableUser).filter_by(userId=userId).first().__dict__
            result = value
            for k, v in value.items():
                try:
                    result[k] = json.loads(v)
                except Exception as e:
                    print(f"ERR Key {k} Value {v}")
                    print(f"ERROR {e}")
            # Remove the item with key "b"
            if "_sa_instance_state" in result:
                del result["_sa_instance_state"]
            return result
        except Exception as e:
            return {'error': f"{e}"}

    @staticmethod
    def getByEmailFromUserDatabase(email: str):
        try:
            value = _session.query(MovableUser).filter_by(email=email).first().__dict__
            result = value
            for k, v in value.items():
                try:
                    result[k] = json.loads(v)
                except Exception as e:
                    print(f"ERR Key {k} Value {v}")
                    print(f"ERROR {e}")
            # Remove the item with key "b"
            if "_sa_instance_state" in result:
                del result["_sa_instance_state"]
            return result
        except Exception as e:
            return {'error': f"{e}"}

    # ******* MovableProvider method call for interacting with database ***********
    @staticmethod
    def logInProvider(result):
        print(F"RESULT : {result}")
        provider = DatabaseManager.getByEmailFromProviderDatabase(result["email"])
        if provider["password"] == result["password"]:
            DatabaseManager.updateProviderDatabase(provider["providerId"], {"isLogIn": True})
            return "Success"
        raise Exception(f"Provider with email {result['email']} and password {result['email']} was not found")

    @staticmethod
    def logOutProvider(result):
        print(F"RESULT : {result}")
        provider = DatabaseManager.getByEmailFromProviderDatabase(result["email"])
        if provider["password"] == result["password"]:
            DatabaseManager.updateProviderDatabase(provider["providerId"], {"isLogIn": False})
            return "Success"
        raise Exception(f"Provider with email {result['email']} and password {result['email']} was not found")

    @staticmethod
    def addToProviderDatabase(provider_model: ProviderModel):
        try:
            _session.add(MovableProvider(provider_model))
            _session.commit()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def updateProviderDatabase(provider_model: str, values: dict):
        try:
            _session.query(MovableProvider).filter_by(providerId=provider_model).update(values)
            _session.commit()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def deleteFromProviderDatabase(provider_model: str):
        try:
            _session.query(MovableUser).filter_by(providerId=provider_model).delete()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def getAllFromProviderDatabase():
        results: list = []
        try:
            for value in _session.query(MovableProvider).all():
                result = value
                for k, v in result.__dict__.items():
                    try:
                        result.__dict__[k] = json.loads(v)
                    except Exception as e:
                        print(f"ERR Key {k} Value {v}")
                        print(f"ERROR {e}")

                # Remove the item with key "b"
                if "_sa_instance_state" in result.__dict__:
                    del result.__dict__["_sa_instance_state"]
                    results.append(result.__dict__)
                else:
                    results.append(result.__dict__)
            return results
        except Exception as e:
            return [{'error': f"{e}"}]

    @staticmethod
    def getByIdFromProviderDatabase(providerId: str):
        try:
            value = _session.query(MovableProvider).filter_by(providerId=providerId).first().__dict__
            result = value
            for k, v in value.items():
                try:
                    result[k] = json.loads(v)
                except Exception as e:
                    print(f"ERR Key {k} Value {v}")
                    print(f"ERROR {e}")
            # Remove the item with key "b"
            if "_sa_instance_state" in result:
                del result["_sa_instance_state"]
            return result
        except Exception as e:
            return [{'error': f"{e}"}]

    @staticmethod
    def getByEmailFromProviderDatabase(email: str):
        try:
            value = _session.query(MovableProvider).filter_by(email=email).first().__dict__
            result = value
            for k, v in value.items():
                try:
                    result[k] = json.loads(v)
                except Exception as e:
                    print(f"ERR Key {k} Value {v}")
                    print(f"ERROR {e}")
            # Remove the item with key "b"
            if "_sa_instance_state" in result:
                del result["_sa_instance_state"]
            return result
        except Exception as e:
            return {'error': f"{e}"}
