import logging

from flask import Blueprint, request

logger = logging.getLogger(__name__)
blueprint = Blueprint("info", __name__)

@blueprint.route("/", methods=["get"])
def get_info():
    return "success", 200
