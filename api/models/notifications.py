import dataclasses
from datetime import datetime
from models.base_model import BaseModel

@dataclasses.dataclass
class Notifications(BaseModel):
    """Representing table auth"""
    __tablename__ = 'notifications'
    title: str
    message: str
    ack: int
    role: str
    created_at: str
    target_user_id: int

    def __init__(self, **kwargs):
        kwargs.setdefault('title', "")
        kwargs.setdefault('message', "")
        kwargs.setdefault('ack', 0)
        kwargs.setdefault('role', "user")
        kwargs.setdefault('created_at', datetime.now())
        super().__init__(**kwargs)
