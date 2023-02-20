from flask_jwt_extended import jwt_required
from models.user import User
from flask import Blueprint, request, make_response, jsonify, abort
from flask_bcrypt import generate_password_hash
from errors import (
    handle_bad_request,
    handle_unauthorized,
    handle_forbidden,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
)

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users",
)


@users_bp.route("/", methods=["GET"])
def fetch_all_users():
    """get all users from database"""
    try:
        users = User.query.order_by(User.username).all()
        users = [
            {
                "id": user.id,
                "username": user.username.format(),
                "display_picture": user.display_picture.format(),
                "user_email": user.user_email.format(),
            }
            for user in users
        ]
        return make_response(jsonify({"users": users, "total_users": len(users)}), 200)
    except Exception as e:
        print(e)
        abort(500)


@users_bp.route("/user/<id>", methods=["GET"])
@jwt_required()
def fetch_specific_user(id):
    """get specific user from database"""
    user = User.query.get_or_404(str(id).strip())
    try:
        user = user.format()
        return make_response(jsonify({"user": user}), 200)
    except Exception as e:
        print(e)
        abort(500)


@users_bp.route("/user/<id>", methods=["PUT"])
@jwt_required()
def update_specific_user(id):
    """update user details in database"""
    data = request.get_json()
    user_to_be_updated = User.query.get_or_404(str(id).strip())
    try:
        new_username = data.get("username")
        new_user_email = data.get("userEmail")
        new_display_picture = data.get("displayPicture")
        new_password = (
            generate_password_hash(data.get("password").strip()).decode("utf-8")
            if data.get("password")
            else None
        )

        user_to_be_updated.update(
            new_username, new_display_picture, new_user_email, new_password
        )
        return make_response(
            jsonify({"success": True, "updated_user": user_to_be_updated.format()}), 200
        )
    except Exception as e:
        print(e)
        abort(500)


@users_bp.route("/user/<id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    """delete a user from the database"""
    user_to_be_deleted = User.query.get_or_404(str(id).strip())
    try:
        user_to_be_deleted.delete()
        return make_response(
            jsonify({"success": True, "message": "User deleted successfully"}), 200
        )
    except Exception as e:
        print(e)
        abort(500)


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
