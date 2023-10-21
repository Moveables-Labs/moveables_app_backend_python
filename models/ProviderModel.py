from dataclasses import asdict, dataclass
from utils.enums import DeliveryMethod


@dataclass
class ProviderModel:
    password:str
    email: str
    id: str = ""
    companyName: str = ""
    phoneNumber: str = ""
    state: str = ""
    dateTime: str = ""

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
