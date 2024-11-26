from typing import Optional

class UserResponseDTO:
    def __init__(self, id: str, name: str, trxId: str):
        self.id = id
        self.name = name
        self.trxId = trxId

    @classmethod
    def from_dict(cls, data: dict) -> "UserResponseDTO":
        return cls(id=data["id"], name=data["name"], trxId=data["trxId"])
