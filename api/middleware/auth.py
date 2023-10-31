from functools import wraps
from services import auth_service
from flask import request, jsonify

def login_required(func):
    @wraps(func)
    def log_req(*args, **kwargs):
        print(f"Middleware executed before {func.__name__}")

        token = request.args.get('token')
        user_id = auth_service.validate_token()
        if user_id is None:
            return jsonify({"error": "Unautorized token"}), 401

        return func(user_id, *args, **kwargs)
    return log_req


def admin_required(func):
    @wraps(func)
    def sign_req(*args, **kwargs):
        print(f"Middleware executed before {func.__name__}")

        token = request.args.get('token')
        user_id = TokenService.get_user_id_by_token(token, 'admin')
        if user_id is None:
            return jsonify({"error": "Unautorized token"}), 401

        return func(user_id, *args, **kwargs)
    return sign_req