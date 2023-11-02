from pydantic import BaseModel

class AuthRequestModel(BaseModel):
    active: int
    password: str
    role: str
    username: str

