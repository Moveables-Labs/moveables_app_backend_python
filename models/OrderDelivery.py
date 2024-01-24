from dataclasses import asdict, dataclass

@dataclass
class OrderModel:
    itemName:str = None
    id:str = None
    itemDetail:str = None
    timeStamp:str = None
    orderStatus:str = None
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""Order(
            itemName = {self.itemName}, 
            id = {self.id}, 
            itemDetail = {self.itemDetail}, 
            timeStamp = {self.timeStamp}, 
            orderStatus = {self.orderStatus}, 
            )"""
        
@dataclass
class DeliveryModel:
    itemName:str = None
    id:str = None
    itemDetail:str = None
    timeStamp:str = None
    deliveryAgent:str = None
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""Order(
            itemName = {self.itemName}, 
            id = {self.id}, 
            itemDetail = {self.itemDetail}, 
            timeStamp = {self.timeStamp}, 
            deliveryAgent = {self.deliveryAgent}, 
            )"""