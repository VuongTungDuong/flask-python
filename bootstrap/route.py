from flask_smorest import Blueprint
from account.route import accout_route

# Api route
api_v1 = Blueprint("v1", "maux", url_prefix="/api/v1")
api_v1.register_blueprint(accout_route)
