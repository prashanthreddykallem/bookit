from models.base_model import BaseModel

class Auth(BaseModel):
    __tablename__ = 'auth'

    def __init__(self, **kwargs):
        kwargs.setdefault('username', "")
        kwargs.setdefault('password', "")
        kwargs.setdefault('active', 1)
        kwargs.setdefault('role', "user")
        kwargs.setdefault('created_at', "2010-10-10 10:10:10")
        super().__init__(**kwargs)

    