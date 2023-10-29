from dataclasses import asdict, dataclass


@dataclass
class FareCostModel:
    fixedPrice:str = None
    costPerMile:str = None
    bookingFee: str = None
    surgePrice: str = None
    tollsFee: str = None
    vat: str = None

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""FareCost(
            fixedPrice = {self.fixedPrice}, 
            costPerMile = {self.costPerMile}, 
            bookingFee = {self.bookingFee}
            surgePrice = {self.surgePrice}
            tollsFee = {self.tollsFee}
            vat = {self.vat}
            )"""