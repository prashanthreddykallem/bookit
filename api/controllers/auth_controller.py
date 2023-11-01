#import json
from flask_cors import cross_origin
from flask import request, jsonify
from middleware.auth import login_required, admin_required
from models.auth import Auth
from models.token import Token
from services import auth_service

# User actions
@cross_origin()
def get_my_token() -> dict:
    """Generate token for a user"""
    username = request.args.get('username')
    password = request.args.get('password')

    try:
        user_id = auth_service.check_login(username, password)
    except Exception:
        return {'error': 'Username or password are invalid'}, 401

    user_token = auth_service.create_token_by_user_id(user_id)
    return {'token': user_token}, 200

@cross_origin()
@login_required
# pylint: disable=unused-argument
def revoke_my_token(user_id: int) -> dict:
    """Delete token for user"""
    token = request.headers.get('Authorization').split()[1]
    auth_service.revoke_token(token)

    return {'status': 'OK'}, 200

@cross_origin()
@login_required
def get_my_data(user_id: int) -> dict:
    """Fetch user_id data"""
    user = Auth.select_first(id=user_id)
    return jsonify(user), 200

@cross_origin()
@login_required
def update_my_data(user_id: int) -> dict:
    """Change values for user_id"""
    # TODO: Change user data from database
    return {'status': 'OK', 'user_id': user_id}

@cross_origin()
@login_required
def close_my_account(user_id: int) -> dict:
    """Make user_id inactive"""
    Auth.update(conditions={'id': user_id}, new_values={'active': 0})
    Token.delete(conditions={'user_id': user_id})
    return {'status': 'OK', 'user_id': user_id}

# Admin actions
@cross_origin()
@admin_required
# pylint: disable=unused-argument
def get_data(admin_id: int, user_id: int) -> dict:
    """Fetch user_id data"""
    user = Auth.select_first(id=user_id)
    return jsonify(user), 200

@cross_origin()
@admin_required
# pylint: disable=unused-argument
def add_user(admin_id: int) -> dict:
    """Fetch user_id data"""
    # TODO: add new user to db based on json body data
    return {'status': 'OK'}

@cross_origin()
@login_required
# pylint: disable=unused-argument
def update_data(admin_id: int, user_id: int) -> dict:
    """Change values for user_id"""
    # TODO: Change user data from database
    return {'status': 'OK', 'user_id': user_id}

@cross_origin()
@login_required
# pylint: disable=unused-argument
def close_account(admin_id: int, user_id:int) -> dict:
    """Make user_id inactive"""
    Auth.update(conditions={'id': user_id}, new_values={'active': 0})
    Token.delete(conditions={'user_id': user_id})
    return {'status': 'OK', 'user_id': user_id}
