from dataclasses import asdict, dataclass

from models.CommunicationDataModel import CommunicationDataModel
from models.LocationModel import LocationModel
from models.OrderDelivery import DeliveryModel
from utils.enums import DeliveryMethod


@dataclass
class ProviderModel:
    providerId: str = None
    isAuth: bool = False
    isLogIn: bool = False
    password: str = None
    email: str = None
    companyName: str = None
    phoneNumber: str = None
    state: str = None
    companyAddress: str = None
    defaultLocation: LocationModel = LocationModel()
    communicationData: CommunicationDataModel = CommunicationDataModel()
    deliveryMethod: DeliveryMethod = DeliveryMethod.NONE.name
    deliveryModel: DeliveryModel = DeliveryModel()

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""ProviderModel(
            companyName = {self.companyName}, 
            phoneNumber = {self.phoneNumber}, 
            state = {self.state}, 
            email = {self.email}, 
            password = {self.password}
        )"""
