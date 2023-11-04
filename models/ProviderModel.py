from dataclasses import asdict, dataclass

from models.CommunicationDataModel import CommunicationDataModel
from models.LocationModel import LocationModel
from models.OrderDelivery import DeliveryModel
from utils.enums import DeliveryMethod


@dataclass
class ProviderModel:
    providerId: str = None
    password: str = None
    email: str = None
    isLogIn: bool = False
    isAuth: bool = False
    companyName: str = None
    phoneNumber: str = None
    state: str = None
    dateTime: str = None
    companyAddress: str = None
    defaultLocation: LocationModel = LocationModel()
    communicationData: CommunicationDataModel = CommunicationDataModel()
    deliveryMethod: DeliveryMethod = DeliveryMethod.NONE
    deliveryModel: DeliveryModel = DeliveryModel()

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""ProviderModel(
            companyName = {self.companyName}, 
            phoneNumber = {self.phoneNumber}, 
            state = {self.state}, 
            email = {self.email}, 
            password = {self.password},
            id = {self.id}
            )"""
