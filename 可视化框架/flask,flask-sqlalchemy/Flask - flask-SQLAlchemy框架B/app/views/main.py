from app.extensions import db
from flask import render_template,Blueprint
from sqlalchemy import *
import json

index = Blueprint("index",__name__)

@index.route("/")
def main():
    return "No problem!"