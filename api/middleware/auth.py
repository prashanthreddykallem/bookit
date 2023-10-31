from functools import wraps
from flask import request, jsonify
from services import auth_service

def login_required(func):
    @wraps(func)
    def log_req(*args, **kwargs):
        print(f"Middleware executed before {func.__name__}")

        try:
            token = request.headers.get('Authorization').split()[1]
            user_id = auth_service.validate_token(token)
        except Exception:
            return jsonify({"error": "Unautorized token"}), 401

        return func(user_id, *args, **kwargs)
    return log_req


def admin_required(func):
    @wraps(func)
    def sign_req(*args, **kwargs):
        print(f"Middleware executed before {func.__name__}")

        try:
            token = request.headers.get('Authorization').split()[1]
            user_id = auth_service.validate_token_role(token, 'admin')
        except Exception:
            return jsonify({"error": "Unautorized token"}), 401

        return func(user_id, *args, **kwargs)
    return sign_req
