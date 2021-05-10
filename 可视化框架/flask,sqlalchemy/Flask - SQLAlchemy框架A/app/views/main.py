from app.settings import session
from flask import Blueprint,render_template
from app.models import Regionsale
from sqlalchemy.sql import func


index = Blueprint("index",__name__)

@index.route("/")
def Demo():
    return "AAA"