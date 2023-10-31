import json
from flask_cors import cross_origin
from middleware.auth import login_required, admin_required
from models import auth, token
from services import auth_service

# Fetch current user data
@cross_origin()
@login_required
def index() -> dict:
    # TODO: Get current logged user data + token
    return {'status': 'OK'}

# Fetch user_id data
@cross_origin()
@admin_required
def user_data(user_id: int) -> dict:
    # TODO: Get user data + token from user_id
    return {'status': 'OK'}

# Add new users
@cross_origin()
@admin_required
def add_user() -> dict:
    # TODO: Add new user to database
    return {'status': 'OK'}

# Change values for user_id
@cross_origin()
def update_user(user_id: int) -> dict:
    # TODO: Change user data from database
    return {'status': 'OK'}

# Make user_id inactive
@cross_origin()
def delete_user(user_id: int) -> dict:
    # TODO: change user active column to inactive
    return {'status': 'OK'}

# Generate token for a user
@cross_origin()
def get_token(username: str, password: str) -> dict:
    try:
        user_id = auth_service.check_login(username, password)
    except:
        return {'error': 'Username or password are invalid'}, 401
    
    user_token = auth_service.create_token_by_user_id(user_id)
    return {'token': user_token}, 200

# Delete token for user
@cross_origin()
def revoke_token(token: str) -> dict:
    auth_service.revoke_token(token)
    return {'status': 'OK'}, 200