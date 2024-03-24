import dataclasses
import json
import logging
from .classes.user import User
from .classes.login_info import LoginInfo
from . import container

from flask import Blueprint, request

logger = logging.getLogger(__name__)
blueprint = Blueprint("login", __name__)

@blueprint.route("/", methods=["post"])
def login():
    username = request.args["username"]
    password = request.args["password"]
    database = container.database

    user: None | User = database.login(LoginInfo(username, password))

    if user is None:
        return "Bad login", 500

    return json.dumps(dataclasses.asdict(user)), 200
