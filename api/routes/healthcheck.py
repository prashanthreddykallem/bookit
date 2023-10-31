from flask import Blueprint
from controllers import health_controller as ctl

health_blueprint = Blueprint('health', __name__)

health_blueprint.route('/', methods=['GET'])(ctl.index)
