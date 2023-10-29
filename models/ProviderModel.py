from dataclasses import asdict, dataclass
from models.CommunicationDataModel import CommunicationDataModel
from models.LocationModel import LocationModel
from models.OrderDelivery import DeliveryModel, OrderModel
from utils.enums import DeliveryMethod


@dataclass
class ProviderModel:
    password:str
    email: str
    id: str = None
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
