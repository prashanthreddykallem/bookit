import hashlib
from models.auth import Auth
from models.token import Token

# Check username and password
# return user_id or rase an exception
def check_login(username: str, password: str) -> int:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = Auth.select_first(username=username, password=hashed_password)
    if user == None:
        raise Exception("Username or password are not valid")
    return user.id

# Validates token
# Returns user_id or rase an exception
def validate_token(token: str) -> int:
    my_token = Token.select_first(token=token)
    if my_token == None:
        raise Exception("invalid token")
    return my_token.user_id

# Create token
def create_token(username: str) -> str:
    user = Auth.select_first(Auth, username=username)
    
    if(user == None):
        raise Exception("Username does not exist")
    
    return create_token_by_user_id(user.id)

# Create token
def create_token_by_user_id(user_id: int) -> str:
    my_token = Token(user_id=user_id)
    my_token.insert()
    return my_token.token

def revoke_token(token: str) -> None:
    Token.delete(token=token)