import hashlib
from models.auth import Auth
from models.token import Token

def check_login(username: str, password: str) -> int:
    """
    Check username and password

    :returns: user_id
    :raises Exception: if not valid
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = Auth.select_first(username=username, password=hashed_password)

    if user is None:
        raise Exception("Username or password are not valid")
    return user.id

def validate_token(token: str) -> int:
    """
    Validates token
    
    :returns: user_id
    :raises Exception: if not valid
    """
    my_token = Token.select_first(token=token)
    if my_token is None:
        raise Exception("invalid token")
    return my_token.user_id

# pylint: disable=unused-argument
def validate_token_role(token: str, role: str) -> int:
    """
    Validates token with role
    
    :returns: user_id
    :raises Exception: if not valid
    """
    user_id = validate_token(token)
    # TODO: Validate role
    return user_id

# Create token
def create_token(username: str) -> str:
    """
    Create token
    
    :returns: token
    :raises Exception: if not valid username
    """
    user = Auth.select_first(username=username)

    if user is None:
        raise Exception("Username does not exist")

    return create_token_by_user_id(user.id)

# Create token
def create_token_by_user_id(user_id: int) -> str:
    """
    Create token
    
    :returns: token
    :raises Exception: if not valid user_id
    """
    my_token = Token.gen_random_token()
    Token.insert(
        user_id=user_id,
        token=my_token
    )
    return my_token

def revoke_token(token: str) -> None:
    Token.delete(token=token)
