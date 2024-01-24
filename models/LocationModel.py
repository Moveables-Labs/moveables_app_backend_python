from dataclasses import asdict, dataclass


@dataclass
class LocationModel:
    pickUpLocation: str = None
    dropOffLocation: str = None
    lastKnowLocation: str = None

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""LocationModel(
            pickUpLocation = {self.pickUpLocation}, 
            dropOffLocation = {self.dropOffLocation}, 
            lastKnowLocation = {self.lastKnowLocation}
            )"""
