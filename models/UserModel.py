from dataclasses import asdict, dataclass
from utils.enums import DeliveryMethod


@dataclass
class UserModel:
    password:str
    email: str
    id: str = ""
    firstName: str = ""
    lastName: str = ""
    phoneNumber: str = ""
    state: str = ""
    dateTime: str = ""
    deliveryMethod: DeliveryMethod = DeliveryMethod.NONE.name

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
            delivertMethod = {self.deliveryMethod}, 
            id = {self.id}
            )"""
