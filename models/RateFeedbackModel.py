from dataclasses import asdict, dataclass


@dataclass
class RateFeedbackModel:
    message:str = None
    timeStamp:str = None
    oneStar:int = None
    twoStar:int = None
    threeStar:int = None
    fourStar:int = None
    fiveStar:int = None
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""ReceiverMessage(
            message = {self.message}, 
            timeStamp = {self.timeStamp}, 
            timeStamp = {self.timeStamp}, 
            oneStar = {self.oneStar},
            twoStar = {self.twoStar},
            threeStar = {self.threeStar},
            fourStar = {self.fourStar},
            fiveStar = {self.fiveStar}
            )"""