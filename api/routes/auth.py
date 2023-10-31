from flask import Blueprint
from controllers import auth_controller

auth_blueprint = Blueprint('auth', __name__)

# myself
auth_blueprint.route('/token', methods=['GET'])(auth_controller.get_my_token)
auth_blueprint.route('/token', methods=['DELETE'])(auth_controller.revoke_my_token)
auth_blueprint.route('/', methods=['GET'])(auth_controller.get_my_data)
auth_blueprint.route('/', methods=['PUT'])(auth_controller.update_my_data)
auth_blueprint.route('/', methods=['DELETE'])(auth_controller.close_my_account)

# admin other users
auth_blueprint.route('/manage/<int:user_id>', methods=['GET'])(auth_controller.get_data)
auth_blueprint.route('/manage', methods=['POST'])(auth_controller.add_user)
auth_blueprint.route('/manage/<int:user_id>', methods=['PUT'])(auth_controller.update_data)
auth_blueprint.route('/manage/<int:user_id>', methods=['DELETE'])(auth_controller.close_account)
