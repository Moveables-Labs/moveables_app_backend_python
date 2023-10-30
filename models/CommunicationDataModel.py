
from dataclasses import asdict, dataclass


@dataclass
class SenderMessage:
    message:str = None
    timeStamp:str = None
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""SenderMessage(
            message = {self.message}, 
            timeStamp = {self.timeStamp}, 
            )"""

@dataclass
class ReceiverMessage:
    message:str = None
    timeStamp:str = None
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""ReceiverMessage(
            message = {self.message}, 
            timeStamp = {self.timeStamp}, 
            )"""


@dataclass
class CommunicationDataModel:
    receiverMessage:ReceiverMessage = None
    senderMessage:SenderMessage = None
    
    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""CommunicationData(
            receiverMessage = {self.receiverMessage}, 
            senderMessage = {self.senderMessage}, 
            )"""