from flask_jwt_extended import jwt_required
from models.models import User
from flask import Blueprint, request

from errors import (
    handle_bad_request,
    handle_unauthorized,
    handle_forbidden,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
)

users_bp = Blueprint(
    "users", __name__, url_prefix="/users", description="Blueprint for users"
)


@users_bp.route("/")
def get():
    """get all users from database"""
    users = User.query.order_by(User.username).all()
    return users, 200


@users_bp.route("/<id>")
@jwt_required()
def get(id):
    """get specific user from database"""
    user = User.query.get_or_404(id)
    return user, 200


@users_bp.route("/user/<id>")
@jwt_required()
def put(id):
    """update user details in database"""
    data = request.get_json()
    user_to_be_updated = User.query.get_or_404(id)
    user_to_be_updated.update(
        data.get("username"),
        data.get("user_email"),
        data.get("password"),
        data.get("profile_image"),
    )
    return user_to_be_updated, 200


@users_bp.route("/user/<id>")
@jwt_required()
def delete(id):
    """delete a user from the database"""
    user_to_be_deleted = User.query.get_or_404(id)
    user_to_be_deleted.delete()
    return user_to_be_deleted, 200


@users_bp.errorhandler(400)
def bad_request_handler(e):
    return handle_bad_request(e)


@users_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized(e)


@users_bp.errorhandler(403)
def forbidden_handler(e):
    return handle_forbidden(e)


@users_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found(e)


@users_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed(e)


@users_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error(e)
