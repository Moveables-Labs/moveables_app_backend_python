from dataclasses import asdict, dataclass


@dataclass
class Transaction():
    history:str = None
    receipt:str = None
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""Transaction(
            history = {self.history}, 
            receipt = {self.receipt}, 
            )"""

@dataclass
class PaymentInfoModel:
    creditCard:str = None
    walletDetail:str = None
    cash:str = None
    transaction = [Transaction().toDict()]
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""PaymentInfo(
            creditCard = {self.creditCard}, 
            walletDetail = {self.walletDetail}, 
            cash = {self.cash}
            )"""
            

