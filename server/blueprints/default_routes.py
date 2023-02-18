from flask import Blueprint, request, jsonify, abort, make_response


default_bp = Blueprint("default", __name__, url_prefix="/api")


@default_bp.route("/hello", methods=["GET"])
def ping_server():
    """test if server is alive"""

    return make_response(
        jsonify({"success": True, "message": "server is running"}), 200
    )
