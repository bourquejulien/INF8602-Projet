import logging
from container import database

from flask import Blueprint, request

logger = logging.getLogger(__name__)
blueprint = Blueprint("login", __name__)

@blueprint.route("/", methods=["post"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    database

    return "success", 200
