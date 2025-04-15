from flask_smorest import Blueprint
from account.controller import account_bp

accout_route = Blueprint("account", __name__, url_prefix="/account")
accout_route.register_blueprint(account_bp)
