import dataclasses
from datetime import datetime
from models.base_model import BaseModel

@dataclasses.dataclass
class Auth(BaseModel):
    """Representing table auth"""
    __tablename__ = 'auth'
    username: str
    password: str
    active: int
    role: str
    created_at: str

    def __init__(self, **kwargs):
        kwargs.setdefault('username', "")
        kwargs.setdefault('password', "")
        kwargs.setdefault('active', 1)
        kwargs.setdefault('role', "user")
        kwargs.setdefault('created_at', datetime.now())
        super().__init__(**kwargs)
