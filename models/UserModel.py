from dataclasses import asdict, dataclass

from models.CommunicationDataModel import CommunicationDataModel
from models.FareCostModel import FareCostModel
from models.LocationModel import LocationModel
from models.OrderDelivery import DeliveryModel, OrderModel
from models.PaymentInfoModel import PaymentInfoModel


@dataclass
class UserModel:
    userId: str = None
    isAuth: bool = False
    isLogIn: bool = False
    password: str = None
    email: str = None
    firstName: str = None
    lastName: str = None
    phoneNumber: str = None
    state: str = None
    address: str = None
    defaultLocation: LocationModel = LocationModel()
    fareCost: FareCostModel = FareCostModel()
    paymentInfo: PaymentInfoModel = PaymentInfoModel()
    communicationData: CommunicationDataModel = CommunicationDataModel()
    order: OrderModel = OrderModel()
    deliveryModel: DeliveryModel = DeliveryModel()

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""UserModel(
            firstName = {self.firstName}, 
            lastName = {self.lastName}, 
            phoneNumber = {self.phoneNumber}, 
            state = {self.state}, 
            email = {self.email}, 
            password = {self.password},
            userId = {self.userId}
            )"""
