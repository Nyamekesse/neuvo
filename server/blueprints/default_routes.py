from flask import Blueprint, current_app, request, jsonify, abort, make_response
from exts import app
import logging

logger = logging.getLogger(__name__)
default_bp = Blueprint("default", __name__, url_prefix="/api")


@default_bp.route("/hello", methods=["GET"])
def ping_server():
    """test if server is alive"""
    # app.logger.info("the ping rout is hit")
    # return make_response(
    #     jsonify({"success": True, "message": "server is running"}), 200
    # )
    try:
        # your code here
        1 / 0  # example exception
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        return "error", 500


@default_bp.route("/test")
def test():
    logger.exception("error")
    raise Exception("This is a test exception")
