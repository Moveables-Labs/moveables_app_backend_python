from dataclasses import asdict, dataclass


@dataclass
class CreateUserModel:
    id: str
    email: str
    password: str

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f"""CreateUserModel(
            email = {self.email}, 
            password = {self.password}, 
            id = {self.id}
            )"""
