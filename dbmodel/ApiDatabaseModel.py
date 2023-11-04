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
        self.defaultLocation = user_model.defaultLocation.toDict()
        self.fareCost = user_model.fareCost.toDict()
        self.paymentInfo = user_model.paymentInfo.toDict()
        self.communicationData = user_model.communicationData.toDict()
        self.order = user_model.order.toDict()
        self.deliveryModel = user_model.deliveryModel.toDict()

    def __repr__(self):
        return f"MovableUser(id={self.id}, email={self.email}, password={self.password}, "


class MovableProvider(_Base):
    __tablename__ = "MovableProvider"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    isAuth = Column(Boolean)
    isLogIn = Column(Boolean)
    password = Column(String)
    dateTime = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, provider_model: ProviderModel):
        self.email = provider_model.email
        self.isAuth = provider_model.isAuth
        self.isLogIn = provider_model.isLogIn
        self.password = provider_model.password

    def __repr__(self):
        return f"MovableProvider(id={self.id}, email={self.email}, password={self.password}, "


_engine = create_engine('sqlite:///dbmodel/apidatabase.db', echo=True)
_Base.metadata.create_all(bind=_engine)
_Session = sessionmaker(bind=_engine)
_session = _Session()


class ApiDatabaseModel:
    @staticmethod
    def addToUserDatabase(user_model: UserModel):
        try:
            _session.add(MovableUser(user_model))
            _session.commit()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def updateUserDatabase(user_model: UserModel):
        try:
            _session.add(MovableUser(user_model))
            _session.commit()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def deleteFromUserDatabase(user_model: UserModel):
        try:
            _session.delete(MovableUser(user_model))
            _session.commit()
            return {"message": "Success", "successCode": 1}
        except Exception as e:
            return {"message": f"{e}", "successCode": 0}

    @staticmethod
    def getAllFromUserDatabase():
        results: list = []
        try:
            for result in _session.query(MovableUser).all():
                # Remove the item with key "b"
                if "_sa_instance_state" in result.__dict__:
                    del result.__dict__["_sa_instance_state"]
                    results.append(result.__dict__)
                else:
                    results.append(result.__dict__)
            print(results)
            return results
        except Exception as e:
            return [{'error': f"{e}"}]

    @staticmethod
    def getByIdFromUserDatabase(userId: str):
        try:
            result = _session.execute(select(MovableUser).filter_by(userId=userId)).first()
            print(result)
            return result
        except Exception as e:
            return [{'error': f"{e}"}]
