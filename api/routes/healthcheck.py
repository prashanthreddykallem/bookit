from flask import Blueprint
from controllers import health_controller

health_blueprint = Blueprint('health', __name__)

health_blueprint.route('/', methods=['GET'])(health_controller.index)