from . import auth
from ..models import User

@auth.route("/")
def index():
    return "Prueba"