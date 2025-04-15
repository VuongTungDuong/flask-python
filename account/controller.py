from flask.views import MethodView
from flask_smorest import Blueprint

account_bp = Blueprint("account", __name__)


@account_bp.route("")
class AccountControler(MethodView):
  def get(self):
    """
    Get One or ALl
    """
    return {"x": "duong"}

  def post(self):
    """
    Create Account
    """
    return {"ok", "ok"}

  def delete(self):
    """
    Delete Account
    """
    return {"ok", "ok"}

  def path(self):
    """
    Update Account
    """
    return {"ok", "ok"}
