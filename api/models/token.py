import secrets
import dataclasses
from datetime import datetime, timedelta
from models.base_model import BaseModel

@dataclasses.dataclass
class Token(BaseModel):
    """Representing table token"""
    __tablename__ = 'token'
    user_id: int
    token: str
    expiration_date: str

    _token_delta = 12

    def __init__(self, **kwargs):
        kwargs.setdefault('user_id', 0)
        kwargs.setdefault('token', Token.gen_random_token())
        kwargs.setdefault('expiration_date', Token.get_delta_date())
        super().__init__(**kwargs)

    @classmethod
    def gen_random_token(cls):
        return secrets.token_urlsafe(16)

    @classmethod
    def get_delta_date(cls):
        return datetime.now() + timedelta(days=cls._token_delta)
