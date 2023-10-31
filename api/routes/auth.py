from flask import Blueprint
from controllers import authController

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(authController.index)
blueprint.route('/', methods=['POST'])(authController.add_user)
blueprint.route('/', methods=['PUT'])(authController.update_user)
blueprint.route('/', methods=['DELETE'])(authController.delete_user)
blueprint.route('/token', methods=['GET'])(authController.get_token)
blueprint.route('/token', methods=['DELETE'])(authController.revoke_token)